# Capstone Project: Predicting UK Racehorses' Risk of Injury Based on Historical Race and Biometric Data

### CURRENT WEEK PLAN: 
- [ DONE ] Create a jupyter notebook for the project
- [ DONE ] Introductary information included
- [ DONE ] Begin to clean the data
- [ DONE ] Exploratory Data Analysis

### NEXT WEEK PLAN:
 - [ ] Exploring Supervised Machine Learning 
 - [ ] Exploring Unsupervised Machine Learning
 - [ ] Upload final project to Synapse when all tasks are complete :tada

## INTRODUCTION: 
This machine learning project hopes to predict UK racehorse injury and decline in peformice using biometric and historical race data. 

### Problem Area:
Horse racing is an expensive and well-sought after sport to watch and participate in. Racehorses go through intense physical activity during their events which can quickly lead to performance decline and at times severe injury due to stress. By predicting injuries in these horses, we can ensure better health for them and in turn mitigate outrageous costs to their owners, and in contrast, even facilitate in their economics wins. 

### Who is Affected:
- Horse Trainers can optimize training and race schedules
- Jockeys can have a better grasp of how their horse is going to be racing day of
- Owners can manage costs and maximize success of their horses
- Veterinarians can possibly use this as helpful insight when caring for the horses

### Impact of the Project:
- Optimize training schedules
- Reduce injury frequency
- Financially helpful

### Data Science Goal:
1. Create a model that can predict race position before incorporating biometric factors
2. Build a predictive model that can help identify injury rish based on performance trends.

#### Repository 
* `data` 
    - contains link to copy of the dataset (stored in a publicly accessible cloud storage)
    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - `joblib` dump of final model(s)

* `notebooks`
    - contains all final notebooks involved in the project

* `docs`
    - contains final report, presentations which summarize the project

* `references`
    - contains papers / tutorials used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `conda.yml`
    - Conda environment specification

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

## Datasets:
https://www.kaggle.com/datasets/hwaitt/horse-racing/data

## INTERPRETATION OF DATA COLUMNS: 
3 Main CSV's

#### BEFORE THE RACE PARAMS:
'pre_racehorse_df':
contains information collected prior a race starts. The odds are averages from from Oddschecker.com, RPRc and TRc also have current values.

####  RACE PARAMS YEARLY:
'race(year)':

rid - Race id

course - Course of the race, country code in brackets, AW means All Weather, no brackets means UK

time - Time of the race in hh:mm format, London TZ

date - Date of the race

title - Title of the race

rclass - Race class

band - Band

ages - Ages allowed

distance - Distance

condition - Surface condition

hurdles - Hurdles, their type and amount

prizes - Places prizes

winningTime - Best time shown

prize - Prizes total (sum of prizes column)

metric - Distance in meters

countryCode - Country of the race

ncond - condition type (created from condition feature)

class - class type (created from rclass feature)

#### HORSE PARAMS YEARLY:

'horse(year)':

horses_* columns description:

rid - Race id

horseName - Horse name

age - Horse age

saddle - Saddle # where horse starts

decimalPrice - 1/Decimal price

isFav - Was horse favorite before start? Can be more then one fav in a race

trainerName - Trainer name

jockeyName - Jockey name

position - Finishing position, 40 if horse didn't finish

positionL - how far a horse has finished from the pursued horse, horses corpses

dist - how far a horse has finished from a winner, horses corpses

weightSt - Horse weight in St

weightLb - Horse weight in Lb

overWeight - Overweight code

outHandicap - Handicap

headGear - Head gear code

RPR - RP Rating

TR - Topspeed

OR - Official Rating

father - Horse's Father name

mother - Horse's Mother name

gfather - Horse's Grandfather name

runners - Runners total

margin - Sum of decimalPrices for the race

weight - Horse weight in kg

res_win - Horse won or not

res_place - Horse placed or not

NOTES: 
Please be aware, the prices provided are the SP (starting prices), and they are not available before race starts. This means prices before start may differ from SP. But usually favorites stay the same, and prices on them often higher then SP. Anyway you can't predict profit with accuracy based only on SP prices.

The listed horse weight is based on the handicap system and decides the weight the horse needs too carry in order to make the race more even, its very common in UK/IRE horse racing. It is not a measurement of the actual horses weight.

### Credits & References
