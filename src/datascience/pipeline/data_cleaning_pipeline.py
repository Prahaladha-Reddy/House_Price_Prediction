from src.datascience.config.configuration import *
from src.datascience.components.data_ingestion import *
from src.datascience.basicConfig import logger
from src.datascience.components.data_cleaning import *


class DataCleaningPipeline:
  def __init__(self):
    pass
  def initiate_data_cleaning(self):
    config=ConfigurationManager()
    data_transform_config=config.get_data_clean()
    data_transform=DataCleaning(config=data_transform_config)
    data_transform.clean()    