clean:
	python src/preprocessing/preprocessing.py

preprocess:
	echo "INFO: Data Preprocessing Started"
	python src/preprocessing/preprocessing.py
	echo "INFO: Data Preprocessing Finished"

model:
	echo "INFO: Modeling started"
	python src/model/model.py
	echo "INFO: modeling Finished"

visualize: