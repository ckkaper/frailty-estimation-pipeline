## Introduction 
This is a small automated pipeline for the evaluation of a sample [Frailsafe](http://frailsafe-project.eu/) dataset. For the data collection a bluetooth beacon device was placed in every room of an elder person's residence. Each elder person is equiped with a wearable  device interacting with the placed beacons around the house. Once the distance between the beacon and the wearable device is small enough a new record is created describing the time and the room of the event. Also for every partitioner, some clinical data are collected containing the health assesment. Aim of this project is to determine the frailty of elder people considering their health status and their movement inside the house. 
-   **beacons dataset**
-   **clinical dataset**

Clean repository
```
make clean
```
Preprocess
```
make preprocess
```

Model
```
make model
```

Visualize 
```
make visualize
```