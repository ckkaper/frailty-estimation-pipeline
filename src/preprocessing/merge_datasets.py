import pandas as pd

# Read datasets for merge
beacons_features = pd.read_csv('./data/preprocessed/beacons_data.csv', sep=';',index_col=1)
clinical_data = pd.read_csv('./data/preprocessed/clinical_data.csv', sep=';',index_col=1)

# Merge datasets
merged_data = pd.merge(clinical_data, beacons_features)

# Save dataset
merged_data.to_csv('./data/preprocessed/merged_dataset.csv', sep=';')

