from src.datascience.config.configuration import *
from src.datascience.components.model_training import *

class ModelTrainingPipeline:
  def __init__(self) -> None:
    pass
  def initiate_model_training(self):
    config=ConfigurationManager()
    model_training_config=config.get_model_training()
    model_trainingg=ModelTraining(config=model_training_config)
    model_trainingg.data_preparation()
    model_trainingg.model_training()