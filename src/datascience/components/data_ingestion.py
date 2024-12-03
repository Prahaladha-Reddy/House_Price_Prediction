from src.datascience.entity.config_entity import *
import urllib.request as request
from src.datascience.basicConfig import logger
from src.datascience.config.configuration import *

class DataIngestion:
  def __init__(self,config:DataIngestionConfig):
    self.config=config
  def download_file(self):
    if not os.path.exists(self.config.local_data_file):
      filename,header=request.urlretrieve(url=self.config.source_url,
                                          filename=self.config.local_data_file)
      logger.info(f'{filename} downloaded! with following info\n{header}')

    else:
      logger.info('File already exists')
