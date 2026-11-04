import streamlit as st
import pandas as pd
import pickle
from pathlib import Path



# Load model
@st.cache_resource
def load_model():
    with open('models/xgboost_smote_gridsearch_model.pkl', 'rb') as f:
        return pickle.load(f)

model = load_model()

# Add CSS styling for decorations
st.markdown("""
    <style>
        .stButton>button {
            background-color:rgb(33, 89, 185);
            color: white;
            font-weight: bold;
            border-radius: 12px;
        }
        .stButton>button:hover {
            background-color:rgb(215, 232, 251);
        }
        h1 {
            color:rgb(10, 69, 36);
            font-family: 'Georgia', serif;
        }
    </style>
""", unsafe_allow_html=True)

# Load and merge data
@st.cache_data
def load_data():
    df_model = pd.read_csv('data/modelling_df.csv')
    df_names = pd.read_csv('data/horse_names.csv')
    df_merged = pd.merge(df_names, df_model, on='Horse_ID')

    # Add day of year
    df_merged["Day_of_Year"] = pd.to_datetime(df_merged["date"]).dt.dayofyear

    return df_merged

df = load_data()

# Absolute path to your image file
img_path = Path(__file__).resolve().parent / "docs" / "horse-image.jpeg"

# Top Banner with Image using st.image
st.image(img_path, width=700, use_container_width=True)

# Build condition ↔ ncond maps
condition_map = df[['condition', 'ncond']].drop_duplicates().set_index('condition')['ncond'].to_dict()
inverse_condition_map = {v: k for k, v in condition_map.items()}

# Title and intro
st.markdown("<h1 style='text-align: center; font-family: 'Georgia', serif;'>Racehorse Non-Finishing Risk Prototype</h1>", unsafe_allow_html=True)
st.write("**Author:** Sabrina del Rosal")
st.markdown("""
This student project models non-finishing outcomes using historical race data. Non-finishing is an injury-risk proxy, not a confirmed injury label. This prototype is not validated for veterinary, training or race-readiness decisions.
""")

# Horse selector
horse_name = st.selectbox("Select a horse", df['horseName'].unique())

# Get selected horse row
horse_row = df[df['horseName'] == horse_name].iloc[0]

# UI-editable features
st.write("### Pre-Race Information")

# Manual inputs with defaults from selected row
age = st.slider("Age", min_value=1, max_value=15, value=int(horse_row['age']), step=1)
saddle = st.number_input("Saddle", value=float(horse_row['saddle']))
OR = st.number_input("Official Rating (OR)", value=int(horse_row['OR']))
weight = st.number_input("Weight", value=int(horse_row['weight']))
hurdles = st.number_input("Hurdles", value=int(horse_row['hurdles']))
metric = st.number_input("Distance (meters)", value=float(horse_row['metric']))

# Condition dropdown and mapping
condition_label = st.selectbox(
    "Track Condition", 
    options=list(condition_map.keys()), 
    index=list(condition_map.keys()).index(horse_row['condition'])
)
ncond = condition_map[condition_label]

class_ = st.number_input("Class", value=int(horse_row['class']))
fences = st.number_input("Fences", value=int(horse_row['fences']))
days_rested = st.number_input("Days Rested", value=float(horse_row['DaysRested']))
races_run = st.number_input("Races Run", value=int(horse_row['RacesRun']))
selected_date = st.date_input("Race Date", value=pd.to_datetime(horse_row['date']))
day_of_year = selected_date.timetuple().tm_yday

# Prepare input DataFrame for model
input_df = pd.DataFrame([{
    'age': age,
    'saddle': saddle,
    'OR': OR,
    'weight': weight,
    'Horse_ID': horse_row['Horse_ID'],
    'condition': condition_label,  # For display/reference
    'hurdles': hurdles,
    'metric': metric,
    'ncond': ncond,
    'class': class_,
    'fences': fences,
    'DaysRested': days_rested,
    'RacesRun': races_run,
    'Day_of_Year': day_of_year
}])

# Drop non-model columns (like 'condition') before prediction
model_input = input_df.drop(columns=['condition'])

# Check for valid numeric input
assert model_input.dtypes.apply(lambda x: x in ['int64', 'float64', 'int32', 'float32']).all(), "Non-numeric values in input!"

# Predict when button is clicked
if st.button("Estimate non-finishing risk"):
    # Perform prediction
    prediction = model.predict(model_input)[0]
    prob = model.predict_proba(model_input)[0][1]  # Model score for non-finishing

    # Display the non-finishing proxy output, without health or race-readiness advice
    st.markdown(f"### **Non-finishing flag**: {'Yes' if prediction == 1 else 'No'}")
    st.write(f"**Model score for non-finishing:** `{prob:.2%}`")
    st.markdown("This is a model output for the non-finishing proxy, not a health or race-readiness assessment.")
