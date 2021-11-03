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

    age, absences, health, studytime, goout, failures, famrel = "", "", "", "", "", "", ""
    if request.is_json:
        age = request.json.get('age',None)
        absences = request.json.get('absences',None)
        health = request.json.get('health',None)
        studytime = request.json.get('studytime',None)
        goout = request.json.get('goout',None)
        failures = request.json.get('failures',None)
        famrel = request.json.get('famrel',None)
        
        if (not age or not absences or not health or not studytime or not goout or not failures or not famrel):
            return jsonify({"msg": "Bad json input. Parameters are missing"}), 400
    else:
        age = request.args.get('age')
        absences = request.args.get('absences')
        health = request.args.get('health')
        studytime = request.args.get('studytime')
        goout = request.args.get('goout')
        failures = request.args.get('failures')
        famrel = request.args.get('famrel')
        if (not age or not absences or not health or not studytime or not goout or not failures or not famrel):
        
            return jsonify({"msg": "Missing query string."}), 400

  
  
 

    data = [[studytime],[absences],[age],[health],[goout],[failures],[famrel]]
    query_df = pd.DataFrame({ 'studytime' : pd.Series(studytime), 'absences' : pd.Series(absences), 'age': pd.Series(age), 'health': pd.Series(health), 
                        'goout': pd.Series(goout), 'failures': pd.Series(failures), 'famrel': pd.Series(famrel)})
    query = pd.get_dummies(query_df)
    prediction = clf.predict(query)
    return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/model.pkl')
    app.run(host="0.0.0.0", debug=True)