import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# import data and remove columns that will not be used for prediction
data = pd.read_csv('./data/raw/clinical_dataset.csv', sep=';').drop(columns=['weight_loss',
                                           'exhaustion_score',
                                           'gait_speed_slower',
                                           'grip_strength_abnormal',
                                           'low_physical_activity'])

# remove outliers
# Method: Replace them with empty values
for columns in data: 
    if (data[columns].dtype == object):
        data[columns].replace('Test not adequate', np.nan, inplace=True)
        data[columns].replace('test non realizable', np.nan, inplace=True)
    elif (data[columns].dtype == np.float64 or data[columns].dtype == np.int64):
        data[columns].replace(999, np.nan, inplace=True)

# Remove null values
# TODO: Remove entries of features with missing values
# TODO: Remove features with many missing values 
# Find rows where there are mon than 1 null value
for column in data:
    # Rplace nan values with the median of each column
    if data[column].dtype != object and data[column].dtype != bool:
        data[column].fillna(data[column].median(), inplace=True)

    # Replace categorical values with the most used column value 
    elif (data[column].dtype != np.float64 and data[column].dtype != np.int64):
         data[column].fillna(data[column].value_counts().index[0], inplace=True)

# Order Categorical Data
# Order categorical data
ordered_categories = {
    'fried': ['Non frail', 'Pre-frail', 'Frail'],
    'gender': ['F', 'M'],
    'gait_optional_binary': [True, False],
    'ortho_hypotension': ['No', 'Yes'],
    'vision': ['Sees well', 'Sees moderately','Sees poorly'  ],
    'audition': ['Hears well', 'Hears moderately', 'Hears poorly' ],
    'weight_loss': ['No', 'Yes'],
    'balance_single': ['>5 sec', '<5 sec'],
    'gait_speed_slower': ['No', 'Yes'],
    'grip_strength_abnormal': ['No', 'Yes'],
    'low_physical_activity': ['No', 'Yes'],
    'memory_complain': ['No', 'Yes'],
    'sleep': ['No sleep problem', 'Occasional sleep problem', 'Permanent sleep problem'],
    'living_alone': ['No', 'Yes'],
    'leisure_club': ['Yes', 'No'],
    'house_suitable_participant': ['Yes', 'No'],
    'house_suitable_professional': ['Yes', 'No'],
    'health_rate': [  '5 - Excellent', '4 - Good', '3 - Medium', '2 - Bad', '1 - Very bad'],
    'health_rate_comparison': [ '5 - A lot better', '4 - A little better', '3 - About the same', '2 - A little worse',
  '1 - A lot worse'],
    'activity_regular': ['> 5 h per week', '> 2 h and < 5 h per week', '< 2 h per week',  'No'],
    'smoking': ['Never smoked', 'Past smoker (stopped at least 6 months)', 'Current smoker']    
}
# encode data
encoder = LabelEncoder()

for column in data:
    if data[column].dtype == np.object or data[column].dtype == np.bool:
        encoder.fit(data[column])
        encoder.classes_ = ordered_categories[column]
        data[column] = encoder.transform(data[column]) 
        
data.to_csv('./data/preprocessed/preprocessed.csv', sep=';')

# split dataset to train and test
data_shape = data.shape[0]

splitter = int(np.ceil(0.8*data_shape))

train_data = data.iloc[:splitter]
test_data = data.iloc[splitter:]

train_data.to_csv('./data/preprocessed/train_data.csv', sep=';')
test_data.to_csv('./data/preprocessed/test_data.csv', sep=';')
