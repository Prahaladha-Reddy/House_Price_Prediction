from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.model_selection import StratifiedKFold
from src.datascience.config.configuration import *
from src.datascience.constants import *
from src.datascience.utils.common import *
from src.datascience.entity.config_entity import *
from src.datascience.basicConfig import logger
import numpy as np
from sklearn.model_selection import RandomizedSearchCV
import pickle






class ModelTraining:
  def __init__(self,config:ModelTrainingConfig):
    self.config=config
  def data_preparation(self):
    self.train_data=pd.read_csv(self.config.cleaned_train_path)
    self.test_data=pd.read_csv(self.config.cleaned_test_path)
    self.X_train=self.train_data.drop(columns=['price'])
    self.y_train=self.train_data['price']
    self.x_test=self.test_data.drop(columns=['price'])
    self.y_test=self.test_data['price']
    self.y_train_log=np.log1p(self.y_train)
    self.y_test_log=np.log1p(self.y_test)
  def model_training(self):
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('regressor', XGBRegressor())
    ])
    param_grid = {
    'regressor__n_estimators': [50, 100, 200], 
    'regressor__learning_rate': [0.01, 0.1, 0.2], 
    'regressor__max_depth': [3, 5, 7], 
    'regressor__subsample': [0.6, 0.8, 1.0], 
    'regressor__colsample_bytree': [0.6, 0.8, 1.0], 
    'regressor__reg_alpha': [0, 0.1, 1],
    'regressor__reg_lambda': [1, 5, 10],
    }
    random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=param_grid,
    n_iter=20, 
    cv=5,  
    scoring='r2',  
    random_state=42,
    n_jobs=-1 
    )
    random_search.fit(self.X_train, self.y_train_log)
    
    with open(self.config.model, 'wb') as file:
      pickle.dump(random_search.best_estimator_, file)

