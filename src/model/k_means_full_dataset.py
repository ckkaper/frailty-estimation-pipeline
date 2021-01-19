import pandas as pd
import numpy as np 
from sklearn.cluster import KMeans 
from sklearn.metrics import   silhouette_score
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 

data = pd.read_csv('./data/preprocessed/merged_dataset.csv', sep=';')
# Cluster data using K-means algorithm. 
results = { 'number_of_clusters': np.arange(2,8), 
      'silhouette_score': [], 
      'PCA_silhouette_score': []}
for i in range(2,8): 
    kmeans = KMeans(n_clusters=i, random_state=0).fit(data)
    labels = kmeans.labels_
    score = silhouette_score(data, labels)
    results['silhouette_score'].append(score)

# Reduce the dimantion of the data and then apply K-means again
for i in range(2,8):
    X = PCA(n_components=2).fit_transform(data)
    kmeans = KMeans(n_clusters=i, random_state=0).fit(X)
    labels = kmeans.labels_
    score = silhouette_score(X, labels)
    results['PCA_silhouette_score'].append(score)

pd.DataFrame(results).to_csv('./data/results/k_means_clustering.csv',sep=';',index=False)