from src.datascience.config.configuration import *
from src.datascience.constants import *
from src.datascience.utils.common import *
from src.datascience.entity.config_entity import *


class DataCleaning:
  def __init__(self,config:DataCleaningConfing):
    self.config=config
  def clean(self):
    self.test_data=pd.read_csv(self.config.test_path)
    self.train_data=pd.read_csv(self.config.test_path)
    self.test_data.reset_index(drop=True,inplace=True)
    self.test_data.drop(columns=['Unnamed: 0'], inplace=True)
    self.train_data.reset_index(drop=True,inplace=True)
    self.train_data.drop(columns=['Unnamed: 0'], inplace=True)    
    save_file(self.test_data,self.config.cleaned_test_path)
    save_file(self.train_data,self.config.cleaned_train_path)
