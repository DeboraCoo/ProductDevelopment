# Librerias
import joblib as jl
import config as cfg
import pandas as pd
import numpy as np

# Carga de data
X_test = pd.read_csv("test.csv")
X_test = X_test[cfg.FEATURES]

# Cargamos modelo y pipeline
titanic_model = jl.load('TitanicPipeline.pkl')

def predict(X):        
        predicts = titanic_model.predict(X)
        #print(predicts)
        result = np.exp(predicts)
        print(result)

predict(X_test)