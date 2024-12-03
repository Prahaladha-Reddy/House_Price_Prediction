from sklearn.model_selection import train_test_split
from src.datascience.config.configuration import *
from src.datascience.constants import *
from src.datascience.utils.common import *
from src.datascience.entity.config_entity import *
from src.datascience.basicConfig import logger


class DataTransform:
  def __init__(self,config:DataTransformConfig):
    self.config=config
  def extract_split(self):
    self.path=self.config.local_data_file
    data=pd.read_csv(self.path)
    self.train,self.test=train_test_split(data,train_size=0.8,random_state=42)
    save_file(self.train,self.config.train_path)
    save_file(self.test,self.config.test_path)
