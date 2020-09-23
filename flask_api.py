# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 00:30:26 2020

@author: Nilesh Suthar

Run Here - http://192.168.43.215:8000/apidocs/   - 192.168.43.215 = Local IP
"""


from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

#It's a Decorator - This will enable Flask. This is a route page.
@app.route('/')
#Basic function on welcome page
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["GET"])
def predict_note_authentication():
    #Below is the valid style of documentation passed for Swagger. Define each input variable.
    #If any input variable not necessary - put required = False
    #Responses means whenever response value meets, print description and output.
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

#This is for input file.
@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)

