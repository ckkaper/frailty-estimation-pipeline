import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.metrics import confusion_matrix

# train model
train_data = pd.read_csv('./data/preprocessed/train_data.csv', sep=';')

tree_classifier = tree.DecisionTreeClassifier(criterion='entropy',
                       max_depth=5,
                       min_samples_leaf=20, min_samples_split=25,
                       min_weight_fraction_leaf=0.0)

X = train_data.drop(['fried','part_id'] ,axis=1)
Y = train_data['fried']

tree_classifier.fit(X, Y)

# make prediction 
test_data = pd.read_csv('./data/preprocessed/test_data.csv', sep=';')

X_test = test_data.drop(['fried','part_id'], axis=1)
Y_pred = tree_classifier.predict(X_test)

# Evaluate results
results = {'id': test_data['part_id'],
                        'Actual': test_data['fried'],
                        'predicted': Y_pred}

conf_m = confusion_matrix(results['Actual'],results['predicted'], normalize='all')
print(np.mean(np.diag(conf_m)))
results = pd.DataFrame({'accurancy': [conf_m]})

print(results['accurancy'][0])

# Save results
results.to_csv('./data/results/decision_trees_classification.csv', sep=';', index=False)


