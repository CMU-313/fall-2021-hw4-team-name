from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     #
     age = request.args.get('age')
     absences = request.args.get('absences')
     health = request.args.get('health')
     studytime = request.args.get('studytime')
     goout = request.args.get('goout')
     failures = request.args.get('failures')
     famrel = request.args.get('famrel')

     data = [[studytime],[absences],[age],[health],[goout],[failures],[famrel]]
     query_df = pd.DataFrame({ 'studytime' : pd.Series(studytime), 'absences' : pd.Series(absences), 'age': pd.Series(age), 'health': pd.Series(health), 
                          'goout': pd.Series(goout), 'failures': pd.Series(failures), 'famrel': pd.Series(famrel)})
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)