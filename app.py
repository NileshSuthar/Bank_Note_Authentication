# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 00:30:26 2020

@author: Nilesh Suthar

Run on your local IP

"""

from flask import Flask, request
import numpy as np
import pickle
import pandas as pd

app = Flask(__name__)
pickle_in = open('classifier.pkl','rb')
classifier = pickle.load(pickle_in)

#It's a Decorator - This will enable Flask. This is a route page.
@app.route('/')
#Basic function on welcome page
def welcome():
    return "Welcome All"

def predict_note_authentication():
    


if __name__ == '__main__':
    app.run(host='0.0.0.0')

