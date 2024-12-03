from src.datascience.entity.config_entity import *
from src.datascience.constants import *
from src.datascience.utils.common import *


class ConfigurationManager:
  def __init__(self,config_filepath=CONFIG_FILE_PATH,
               schema_filepath=SCHEMA_FILE_PATH,
               params_filepath=PARAMS_FILE_PATH):
    print(schema_filepath)
    self.config=read_yaml(config_filepath)
    self.schema=read_yaml(schema_filepath)
    self.params=read_yaml(params_filepath)
    crate_directories([self.config.artifacts_root])
  def get_data_ingestion_config(self)->DataIngestionConfig:
    config=self.config.data_ingestion
    crate_directories([config.root_dir])
    data_ingestion_config=DataIngestionConfig(
      root_dir=config.root_dir,
      source_url=config.source_url,
      local_data_file=config.local_data_file,
      unzip_dir=config.unzip_dir
    )
    return data_ingestion_config
  def get_data_transform(self)->DataTransformConfig:
    config=self.config.data_transform
    crate_directories([config.root_dir])
    data_trainsform_config=DataTransformConfig(
    root_dir=config.root_dir,
    local_data_file=config.local_data_file,
    train_path=config.train_path,
    test_path= config.test_path
    )
    return data_trainsform_config
  def get_data_clean(self)->DataCleaningConfing:
    config=self.config.data_cleaning
    crate_directories([config.root_dir])
    data_clean_config=DataCleaningConfing(
       root_dir= config.root_dir ,
        train_path= config.train_path ,
        test_path = config.test_path ,
        cleaned_train_path= config.cleaned_train_path ,
        cleaned_test_path= config.cleaned_test_path ,
    )
    return data_clean_config
  def get_model_training(self)->ModelTrainingConfig:
    config=self.config.model_training
    crate_directories([config.root_dir])
    Model_Training_config=ModelTrainingConfig(
      root_dir=config.root_dir,
      cleaned_train_path=config.cleaned_train_path,
      cleaned_test_path=config.cleaned_test_path,
      model=config.model
    )
    return Model_Training_config
  def get_model_evaluation(self)->ModelValidationConfig:
    print('Hitting the get model_evaluation')
    config=self.config.model_validation
    print('got model_validation')
    crate_directories([config.root_dir])
    print('creatig')
    Model_Validation_config=ModelValidationConfig(
      root_dir=config.root_dir,
      scores=config.scores,
      cleaned_test_path=config.cleaned_test_path,
      model=config.model,
      ResidualDistribution=config.ResidualDistribution,
      ResidualsVSPredictions=config.ResidualsVSPredictions
      
    )
    return Model_Validation_config