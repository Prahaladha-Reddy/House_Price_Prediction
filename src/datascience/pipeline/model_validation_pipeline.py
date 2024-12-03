from src.datascience.config.configuration import *
from src.datascience.components.model_validation import *

class ModelTrainingPipeline:
  def __init__(self) -> None:
    pass
  def initiate_model_training(self):
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