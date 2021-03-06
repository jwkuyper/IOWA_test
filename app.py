# -*- coding: utf-8 -*-

import os
import pandas as pd

import json

from flask import Flask
from flask_restful import Api, Resource, request
import joblib


port = int(os.getenv('PORT', '5000'))

app = Flask(__name__)
api = Api(app)

# argument parsing
#parser = reqparse.RequestParser()
#parser.add_argument('query')




class PredictRegression(Resource):
    def get(self):
        model_path = 'lrteam1.pkl'
        with open(model_path, 'rb') as f:
            regression_model = joblib.load(f)
                
        # get the query parameters
        #param = request.args.get('param')
        params = request.args

        independents=pd.DataFrame(params,index=[0])
              
        # make a prediction
        predictions = regression_model.predict(independents)
       
        # create JSON object
        #pd.DataFrame(predictions, columns=['Prediction'])
        output = pd.DataFrame(predictions, columns=['Prediction']).to_json(orient='table')
        output=json.loads(output)
        
        return output
    
    def post(self):
        model_path = 'lrteam1.pkl'
        with open(model_path, 'rb') as f:
            regression_model = joblib.load(f)
                
        # get the form data
        params = request.form

        independents=pd.DataFrame(params,index=[0])
              
        # make a prediction
        predictions = regression_model.predict(independents)
       
        # create JSON object
        #pd.DataFrame(predictions, columns=['Prediction'])
        output = pd.DataFrame(predictions, columns=['Prediction']).to_json(orient='table')
        output=json.loads(output)
        
        return output

# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictRegression, '/regression')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=port)
    
#Postman: http://127.0.0.1:5000/regression?iso_code=103&total_cases=32364&total_deaths=548&new_deaths=6&total_cases_per_million=601.882&new_cases_per_million=4.575&total_deaths_per_million=10.191&new_deaths_per_million=0.112&new_tests=3381&total_tests=425364&total_tests_per_thousand=7.911&new_tests_per_thousand=0.063&population=53771300&median_age=20&life_expectancy=66.7
    