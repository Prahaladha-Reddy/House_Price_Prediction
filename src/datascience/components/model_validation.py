from src.datascience.entity.config_entity import *
import os
import urllib.request as request
from src.datascience.basicConfig import logger
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.model_selection import RandomizedSearchCV
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from src.datascience.constants import *
from src.datascience.utils.common import *
import pickle
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import median_absolute_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_log_error
import seaborn as sns
import matplotlib.pyplot as plt
from src.datascience.config.configuration import *
from src.datascience.constants import *
from src.datascience.utils.common import *
from src.datascience.entity.config_entity import *
from src.datascience.basicConfig import logger



class ModelValidation:
  def __init__(self,config:ModelValidationConfig):
    self.config=config
    
  def model_load(self):
    with open(self.config.model, 'rb') as file:
      self.loaded_model = pickle.load(file)
  def predict(self):
    data=pd.read_csv(self.config.cleaned_test_path)
    self.x_test=data.drop(columns=['price'])
    self.y_test=data['price']
    self.y_pred_log= self.loaded_model.predict(self.x_test)
    self.y_pred=np.expm1(self.y_pred_log)
  def scores(self):
    mae = mean_absolute_error(self.y_test, self.y_pred)
    mse = mean_squared_error(self.y_test, self.y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(self.y_test, self.y_pred)
    mape = np.mean(np.abs((self.y_test - self.y_pred) / self.y_test)) * 100
    smape = np.mean(2 * np.abs(self.y_test - self.y_pred) / (np.abs(self.y_test) + np.abs(self.y_pred))) * 100
    median_ae = median_absolute_error(self.y_test, self.y_pred)
    explained_variance = explained_variance_score(self.y_test, self.y_pred)
    max_error = np.max(np.abs(self.y_test - self.y_pred))
    n = len(self.y_test)
    k = self.x_test.shape[1]
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - k - 1)
    quantiles = np.quantile(self.y_test, [0.25, 0.5, 0.75])
    for q in quantiles:
        subset = self.y_test[self.y_test <= q]
        r2_subset = r2_score(subset, self.y_pred[self.y_test <= q])
    msle = mean_squared_log_error(self.y_test, self.y_pred)
    results = {
    "MAE": mae,
    "MSE": mse,
    "RMSE": rmse,
    "R²": r2,
    "Adjusted R²": adjusted_r2,
    "MAPE": mape,
    "SMAPE": smape,
    "Median AE": median_ae,
    "Explained Variance": explained_variance,
    "Max Error": max_error,
    "MSLE": msle
      }
    self.results = pd.DataFrame(list(results.items()), columns=["Metric", "Value"])
    save_file(self.results,self.config.scores)
  
    print('scores is successful')
    
  def plots(self):
    residuals = self.y_test - self.y_pred
    # Residual Distribution Plot
    plt.figure()
    sns.histplot(residuals, kde=True)
    plt.title("Residual Distribution")
    plt.xlabel("Residuals")
    plt.ylabel("Frequency")
    plt.grid()
    plt.savefig(self.config.ResidualDistribution, dpi=300)
    plt.close()

    # Residuals vs Predictions Plot
    plt.figure()
    plt.scatter(self.y_pred, residuals, alpha=0.6)
    plt.axhline(0, color='red', linestyle='--')
    plt.title("Residuals vs. Predictions")
    plt.xlabel("Predicted Values")
    plt.ylabel("Residuals")
    plt.grid()
    plt.savefig(self.config.ResidualsVSPredictions, dpi=300)
    plt.close()








    


