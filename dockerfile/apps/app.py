from flask import Flask, jsonify, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def hello():
    return "try the predict route it is great!! TESTING REDEPLOYMENT"

@app.route('/predict')
def predict():
	 #use entries from the query string here but could also use json
     age = request.args.get('age')
     absences = request.args.get('absences')
     health = request.args.get('health')
     freetime = request.args.get('freetime')
     studytime = request.args.get('studytime')
     data = [[age],[health],[absences],[freetime],[studytime]]
     query_df = pd.DataFrame({ 'age' : pd.Series(age) ,'health' : pd.Series(health) ,'absences' : pd.Series(absences), 
                                'freetime' : pd.Series(freetime), 'studytime' : pd.Series(studytime)})
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify(np.asscalar(prediction))

if __name__ == '__main__':
    clf = joblib.load('/apps/newModel.pkl')
    app.run(host="0.0.0.0", debug=True)