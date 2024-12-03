from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
  root_dir:Path
  source_url:str
  local_data_file:Path
  unzip_dir:Path


@dataclass
class DataTransformConfig:
  root_dir:Path
  local_data_file: Path
  train_path: Path
  test_path: Path


@dataclass
class DataCleaningConfing:
  root_dir: Path
  train_path: Path
  test_path: Path
  cleaned_train_path: Path
  cleaned_test_path: Path


@dataclass
class ModelTrainingConfig:
  root_dir:Path
  cleaned_train_path: Path
  cleaned_test_path: Path
  model:Path  

@dataclass
class ModelValidationConfig:
    root_dir: Path
    cleaned_test_path:Path
    model: Path
    scores: Path
    ResidualDistribution: Path
    ResidualsVSPredictions: Path
