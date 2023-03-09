from flask import Flask, request, jsonify
import joblib
from score import score
app = Flask(__name__)
from textblob import TextBlob
import pytest
import os







@app.route('/score', methods=['POST'])

def score_text_1():
    
    os.system('pytest --cov=. --cov-report=term-missing --cov-report=html > coverage.txt &')
    
    response = {'prediction': int(0), 'propensity': "hjk"}
    print(response)
    return jsonify(response)

@app.get('/shutdown')
def shutdown():
    app.shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
