# Librerias
import joblib as jl
import config as cfg
import pandas as pd
import numpy as np

# Cargamos modelo y pipeline
titanic_model = jl.load('TitanicPipeline.pkl')

def predict(X):        
        X = X[cfg.FEATURES]
        predicts = titanic_model.predict(X)
        result = np.exp(predicts)
        return result