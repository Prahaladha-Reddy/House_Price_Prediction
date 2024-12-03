
from src.datascience.pipeline.data_ingestion_pipeline import *
from src.datascience.pipeline.data_cleaning_pipeline import *
from src.datascience.pipeline.data_transformation_pipeline import *

from src.datascience.pipeline.model_training_pipeline import *

from src.datascience.pipeline.model_validation_pipeline import *
from src.datascience.pipeline.prediction_pipeline import *
from src.datascience.basicConfig import logger


STAGE_NAME='Data Ingestion Stage'

try:
  logger.info(f'>> Stage {STAGE_NAME} started >>')
  obj=DataIngestionTrainingPipeline()
  obj.initiate_data_ingestion()
  logger.info(f'>> stage {STAGE_NAME} completed >> \n\nx===x')
except Exception as e:
  logger.exception(e)
  raise e


STAGE_NAME='Data Transform Stage'

if __name__ == '__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME}')
        config=ConfigurationManager()
        data_transform_config=config.get_data_transform()
        data_transform=DataTransform(config=data_transform_config)
        data_transform.extract_split()
        logger.info(f'>> stage {STAGE_NAME} completed')
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME='Data Cleaning Stage'

if __name__ == '__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME}')
        config=ConfigurationManager()
        data_transform_config=config.get_data_clean()
        data_transform=DataCleaning(config=data_transform_config)
        data_transform.clean()
        logger.info(f'>> stage {STAGE_NAME} completed')
    except Exception as e:
        logger.exception(e)
        raise e
    

STAGE_NAME='Model training Stage'

if __name__ == '__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME}')
        config=ConfigurationManager()
        model_training_config=config.get_model_training()
        model_trainingg=ModelTraining(config=model_training_config)
        model_trainingg.data_preparation()
        model_trainingg.model_training()
        logger.info(f'>> stage {STAGE_NAME} completed')
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME='Model validation Stage'

if __name__ == '__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME}')
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation()  # Correct config retrieval
        model_evaluationn=ModelValidation(config=model_evaluation_config) 
        model_evaluationn.model_load()
        print('success1')
        model_evaluationn.predict()
        print('success2')
        model_evaluationn.scores()
        print('success3')
        model_evaluationn.plots()
        logger.info(f'>> stage {STAGE_NAME} completed')
    except Exception as e:
        logger.exception(e)
        raise e
    
STAGE_NAME='Model validation Stage'

if __name__ == '__main__':
    try:
        logger.info(f'>> stage {STAGE_NAME}')
        config=ConfigurationManager()
        model_evaluation_config=config.get_model_evaluation()  # Correct config retrieval
        model_evaluationn=ModelValidation(config=model_evaluation_config) 
        model_evaluationn.model_load()
        print('success1')
        model_evaluationn.predict()
        print('success2')
        model_evaluationn.scores()
        print('success3')
        model_evaluationn.plots()
        logger.info(f'>> stage {STAGE_NAME} completed')
    except Exception as e:
        logger.exception(e)
        raise e
    


