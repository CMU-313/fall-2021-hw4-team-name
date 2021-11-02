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

    age, absences, health = "", "", ""
    if request.is_json:
        age = request.json.get('age', None)
        absences = request.json.get('absences', None)
        health = request.json.get('health', None)
        if (not age or not absences or not health):
            return jsonify({"msg": "Bad json input. Parameters are missing"}), 400
    else:
        age = request.args.get('age')
        absences = request.args.get('absences')
        health = request.args.get('health')
        if (not age or not absences or not health):
            if not request.is_json:
                return jsonify({"msg": "Missing query string. ZZZ"}), 400

       

    data = [[age],[health],[absences]]
    query_df = pd.DataFrame({ 'age' : pd.Series(age) ,'health' : pd.Series(health) ,'absences' : pd.Series(absences)})
    query = pd.get_dummies(query_df)
    prediction = clf.predict(query)
    return jsonify(np.asscalar(prediction)), 200


  
  
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