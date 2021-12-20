# Librerias
import joblib as jl
import config as cfg
import pandas as pd
import numpy as np

# Carga de data
X_test = pd.read_csv("marketing_campaign.tsv", sep='\t', engine='python')
X_test = X_test[cfg.FEATURES]

# Cargamos modelo y pipeline
marketing_model = jl.load('MarketingPpipeline.pkl')

def predict(X):        
        predicts = marketing_model.predict(X)
        #print(predicts)
        result = predicts
        print(result)

predict(X_test)