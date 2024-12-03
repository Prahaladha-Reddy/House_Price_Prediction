from src.datascience.config.configuration import *
from src.datascience.basicConfig import logger
from src.datascience.components.data_transformation import *




class DataTransformationTrainingPiprline:
  def __init__(self):
   pass
  def  initiate_data_transformation(self):
    config=ConfigurationManager()
    data_transform_config=config.get_data_transform()
    data_transform=DataTransform(config=data_transform_config)
    data_transform.extract_split()