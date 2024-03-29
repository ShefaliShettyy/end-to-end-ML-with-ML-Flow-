# end-to-end-ML-with-ML-Flow-
## Workflows

1. Update config.yaml                             --->download the dataset and save in folder
2. Update schema.yaml                             --->schema is all the column
3. Update params.yaml                             ---> parameters
4. Update the entity                              --->config variables are declared and returned here
5. Update the configuration manager in src config ---> read all the config files and creating artifac folder by calling it from config and return those path(config)
6. Update the components                          ---> data ingestion(download, unzip), validation etc
7. Update the pipeline                            --->all the components will be integrating with the pipeline ->training pipeline ->prediction pipeline
8. Update the main.py
9. Update the app.py                              ---> UI functionality 

constants --> has path of config, params, schema