import matplotlib.pyplot as plt
import pandas as pd

results = pd.read_csv('./data/results/k_means_clustering.csv', sep=';')

# Plot Silhouette value of the two approaches
plt.xlabel('number of clusters')
plt.ylabel('score')
 
plt.plot(results['number_of_clusters'], results['silhouette_score'],"-b", label='silohoutte score')
plt.plot(results['number_of_clusters'], results['PCA_silhouette_score'], "-r",label="PCA silhouette score")
plt.legend(loc="upper right")
plt.show()