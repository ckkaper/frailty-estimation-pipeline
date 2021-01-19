clean:
	# python src/clean.py

preprocessing:	
ifeq ($(dataset), clinical)
	echo "INFO: Preprocessing of clinical dataset"
	python src/preprocessing/clinical_dataset.py
	echo "INFO: Preprocessing completed"
endif
ifeq ($(dataset), beacons)
	echo "INFO: Preprocessing of beacons dataset"
	python src/preprocessing/beacons_dataset.py
	echo "INFO: Preprocessing completed"
endif
ifeq ($(dataset), merge)
	echo "INFO: Merging datasets"
	python src/preprocessing/merge_datasets.py
	echo "INFO: Merging completed"
endif

	echo "INFO: Data Preprocessing Finished"

model:
ifeq ($(model), decision_trees)
	echo "INFO: Running $(model) model"
	python src/model/decision_trees_clinical_dataset.py
	echo "INFO: Modeling completed"
endif
ifeq ($(model), k_means)
	echo "INFO: Running $(model) model"
	python src/model/k_means_full_dataset.py
	echo "INFO: Modeling completed"
endif


visualize:
ifeq ($(tast), 'kala')
	echo "one"
endif

clustering:
	echo "Start of Clustering Pipeline"
	python src/clean.py
	echo "Preprocessing clinical dataset"
	python src/preprocessing/clinical_dataset.py
	echo "Preprocessing beacons dataset"
	python src/preprocessing/beacons_dataset.py
	echo "merge"
	python src/preprocessing/merge_datasets.py
	echo "model"
	python src/model/k_means_full_dataset.py
	echo "visualize"
	python src/visualization/clustering.py


classification:
	echo "Start Classification Pipeline"
	python src/clean.py
	echo "Preprocessing clinical dataset"
	python src/preprocessing/clinical_dataset.py
	echo "Model using decision trees"
	python src/model/decision_trees_clinical_dataset.py