import pandas as pd

# merge beacons with clinical dataset
beacons_features = pd.read_csv('./data/preprocessed/beacons_data.csv', sep=';')
clinical_data = pd.read_csv('./data/preprocessed/clinical_data.csv', sep=';')

merged_data = pd.merge(beacons_features, clinical_data)

merged_data.to_csv('./data/preprocessed/merged_dataset.csv', sep=';', index=False)