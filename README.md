# end-to-end-ML-with-ML-Flow-
## Workflows

1. Update config.yaml                             --->download the dataset and save in folder
2. Update schema.yaml                             --->
3. Update params.yaml                             ---> parameters
4. Update the entity                              --->config variables are declared and returned here
5. Update the configuration manager in src config ---> read all the config files and creating artifac folder by calling it from config and return those path(config)
6. Update the components                          ---> data ingestion(download, unzip), validation etc
7. Update the pipeline                            --->all the components will be integrating with the pipeline ->training pipeline ->prediction pipeline
8. Update the main.py
9. Update the app.py                              ---> UI functionality 

constants --> has path of config, params, schema

data ingestion: we take data and create folder artifacts, download dataset into artifacts and unzip it
data validation: we take the dataset from artifacts , EDA, and create validation folder in arifacts and return true or false as status

1. Update config.yaml                             --->dataset from artifaces path , status which say validation is true or false
2. Update schema.yaml                             --->column names, data type, target variable
3. Update params.yaml                             ---> 
4. Update the entity                              --->
5. Update the configuration manager in src config ---> 
6. Update the components                          --->check if the column name is same or compare the column name with schema and return True
7. Update the pipeline                            --->
8. Update the main.py
9. Update the app.py 

dataTransformation:

1. Update config.yaml                             --->root_dir, data_path  path
2. Update schema.yaml                             --->
3. Update params.yaml                             ---> 
4. Update the entity                              ---> root_dir, data_path instaiallized inside class
5. Update the configuration manager in src config ---> read the config schema params, get the data():
6. Update the components                          ---> train_test_split, encoder technique
7. Update the pipeline                            --->
8. Update the main.py
9. Update the app.py

ModelTraining:

1. Update config.yaml                             --->Train.csv, Test.csv, modelname=joblib(after training)
2. Update schema.yaml                             --->
3. Update params.yaml                             ---> 
4. Update the entity                              ---> alpha and L1 (PARAMS), TRAIN, TEST
5. Update the configuration manager in src config ---> 
6. Update the components                          ---> 
7. Update the pipeline                            --->
8. Update the main.py
9. Update the app.py 

https://github.com/ShefaliShettyy/end-to-end-ML-with-ML-Flow-.git
https://dagshub.com/ShefaliShettyy/end-to-end-ML-with-ML-Flow-.mlflow