## Introduction 
This is a small automated pipeline for the evaluation of a sample [Frailsafe](http://frailsafe-project.eu/) dataset. For the data collection a bluetooth beacon device was placed in every room of an elder person's residence. Each elder person is equiped with a wearable  device interacting with the placed beacons around the house. Once the distance between the beacon and the wearable device is small enough a new record is created describing the time and the room of the event. Also for every partitioner, some clinical data are collected containing the health assesment. Aim of this project is to determine the frailty of elder people considering their health status and their movement inside the house. 
-   **beacons dataset**
-   **clinical dataset**

## Preprocessing 
Bellow are presented the preprocessing methods followed on preprocessing the data.
```
make preprocessing dataset=${clinical,beacons}
```
### Clinical Dataset
For the clincal dataset the following columns are stripped out, since the aim is to predict the fraility of a person without the information gained from this data. 
```
 'weight_loss'
 'exhaustion_score'
 'gait_speed_slower'
 'grip_strength_abnormal'
 'low_physical_activity'
```
Following,  outliers where removed by replacing invalid values with `NaN`. To detect the outlier values the histogram method was used manually in each column an the unique function as well. Subsequently, each missing value of the dataset is replaced by the most frequent value of the current feature. For categorical data a data labeling approach was incorporated where numerical labels where assigned to each categorical value. Here is worth noting that before the labeling process the categorical data where ordered in terms of which leads to higher degree of frailty .

### Beacons Data
For the beacons dataset the following lines where also stripped out since it is assumed that the time and the date of the beacon event will not contribute in the feature extraction. For the feature generation,  the percentage of the time each person spent on a room is calculated by dividing the records on that particular room with the total records of the user. 
```
'ts_date'
'ts_time'
```
Other interventions made to the data where to remove invalid users. Also room entries infering the same group where labeled with one value.    

## Model 
### Classification
#### Method
Decision trees algorithm is used in order to perform classification of the clinical dataset. To train the model 80 percent of the dataset is used for training and 20 percent is used for test. For the decision tree best hyperparameter estimation a gridsearch algorithm resulted with the following values: 
```
criterion: 'entropy'
max_depth: 5
min_samples_leaf: 20
min_samples_split: 25
min_weight_fraction_leaf: 0.0
```
#### Results
The approach mentioned above yilded 0.206 of average classification score to all groups while the best score was 0.55 (See results in `./data/results` directory.). 
Also other approaches using different parameters where used for this particular algorithm but yilded poorer results (See `./docs/report.json`).


To run the pipeline you can use the following command
```
make classification
```
### Clustering
#### Method
For the clustering of the data, both datasets where merged into since they referenced to the same partitioner. Kmeans clustering algorithm is used to cluster the data. For the evaluation of the algorithm silhouette score is used as a metric. Also, in order to determine the nubmer of clusters best fit the data multiple runs of the algorithm where performed on clusters from 2 to 8. Also for better clustering Principal Component Analysis was also performed on our data in order to reduce the dimentionality of our data. For the Principal Component Analysis the most 2 significant component where used for each feature. 

#### Results
The results for these approaches are demonstrated in the following figure, where as illustrated the dimentionality reduction reduces increases the silhouette score and the best number of clusters is 2.

![K-means](/docs/figures/clustering_metrics.jpg)

The results are saved in `./data/results` directory.

Use the following algorithm in order to perform 
```
make clustering
```

## Notes
Below are some instruction about the project structure: 
1. Preprocessed datasets can be found in `./data/preprocessed` directory
2. Preprocessing steps for both algorithms can be found inside `./src/preprocessing`
3. Models are located in `./src/models`
4. **Jupyer Notebook** also used for the analysis and the visualization, notebooks are located in `./notebooks`
5. In `./docs/report.json ` a summary of each method along with each resutls is reported. 
