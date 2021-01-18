import pandas as pd
from sklearn import tree
from sklearn.metrics import confusion_matrix

# train model
train_data = pd.read_csv('./data/preprocessed/train_data.csv', sep=';')

tree_classifier = tree.DecisionTreeClassifier()
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

results = pd.DataFrame({'accurancy': [confusion_matrix(results['Actual'],results['predicted'], normalize='all')]})

# Save results
results.to_csv('./data/results/decision_trees_classification.csv', sep=';')


