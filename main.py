from textsumm.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline
#from textsumm.pipeline.stage_2_data_validation import DataValidationTrainingPipeline
#from textsumm.pipeline.stage_3_data_transformation import DataTransformationTrainingPipeline
#from textsumm.pipeline.stage_4_model_trainer import ModelTrainerTrainingPipeline
#from textsumm.pipeline.stage_5_model_evaluation import ModelEvaluationTrainingPipeline
from textsumm.logging import logger


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e