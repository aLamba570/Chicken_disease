from CNN_Classifier import logger
from CNN_Classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from CNN_Classifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

print("Starting the application...")
try:
    print(f"Starting {STAGE_NAME}...")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    print(f"Completed {STAGE_NAME} successfully!")
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    print(f"Error occurred: {str(e)}")
    logger.exception(e)
    raise e


STAGE_NAME="Prepare base model"
try:
    print(f"Starting {STAGE_NAME}.....")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    print(f"Completed {STAGE_NAME} successfully!")
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    print(f"Error occurred: {str(e)}")
    logger.exception(e)
    raise e





