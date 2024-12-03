import pickle
import numpy as np
import pandas as pd
from pathlib import Path

class PredictionPipeline:
  def __init__(self):
    with open(Path('artifacts/model_train/model.pkl'), 'rb') as file:
      self.loaded_model = pickle.load(file)
  def predict(self,data):
    self.prediction=self.loaded_model.predict(data)
    self.y_pred=np.expm1(self.prediction)
    return self.y_pred
    