import os
import yaml
import sys
from ..basicConfig import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError
from pathlib import Path
import yaml
from box.exceptions import BoxValueError
from ensure import ensure_annotations
import pandas as pd
@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    try:
        # Ensure path is resolved to an absolute path
        path_to_yaml = Path(path_to_yaml).resolve()

        # Check if the file exists
        if not path_to_yaml.exists():
            raise FileNotFoundError(f"YAML file not found at {path_to_yaml}")

        # Open and read the YAML file
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)  # Pass the file object, not the path
            logger.info(f"YAML file {path_to_yaml} is loaded safely")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"{path_to_yaml}  YAML file is empty")
    except Exception as e:
        logger.error(f"Error while reading YAML: {e}")
        raise e

@ensure_annotations
def crate_directories(path_to_directories:list, verbose=True):
  for path in path_to_directories:
    os.makedirs(path,exist_ok=True)
    if verbose:
      logger.info(f'Created directory {path}')
    
@ensure_annotations
def save_json(path,data:dict):
  with open(path) as f:
    content=json.load(f)
    logger.info(f"json file loaded succesfully from: {path}")
    return ConfigBox(content)    

@ensure_annotations
def save_bin(data: Any,path:Path):
  joblib.dump(value=data,filename=path)
  logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path:Path):
  data=joblib.load(path)
  logger.info(f"binary file loaded from: {path}")
  return data 


def save_file(DataFrame, path):
    # Ensure the directory exists
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Save the DataFrame as a CSV
    DataFrame.to_csv(path, index=False, header=True)
    logger.info(f"File saved successfully at {path}")

