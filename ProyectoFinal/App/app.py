import pandas as pd
import json
from pandas.core.frame import DataFrame
from flask import Flask, jsonify, request

#import pipeline_predict as pp
import script as pp
app = Flask(__name__)


@app.route("/saludar")
def saludar():
    return jsonify({"username":"debora coo"})

#Ruta para predecir
@app.route("/predecir", methods=['POST'])
def predict_from_pp():
    json_data = request.get_json()
    json_data = json.dumps(json_data)
    json_data = json.loads(json_data)

    dataframe = pd.DataFrame.from_dict(json_data, orient="index")        
    resultado = pp.predict(dataframe.T)    
    return jsonify({"Prediccion": resultado[0]})