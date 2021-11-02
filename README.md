# Team Name HW4

## API instructions:

**Make sure you have deployed the microservice properly first**
To use the microservice navigate to http://localhost:5000/predict?studytime=A&absences=B&age=C&health=D&goout=E&failures=F&famrel=G

You will have to change the variables A,B,C,D,E,F,G to their appropriate values.

A ranges from 1-4
B ranges from 0-93
C ranges from 15-22
D ranges from 1-5
E ranges from 1-5
F ranges from 1-4
G ranges from 1-5

The variables meanings can be found below

A: studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
B: absences - number of school absences (numeric: from 0 to 93)
C: age - student's age (numeric: from 15 to 22)
D: health - current health status (numeric: from 1 - very bad to 5 - very good)
E: goout - going out with friends (numeric: from 1 - very low to 5 - very high)
F: failures - number of past class failures (numeric: n if 1<=n<3, else 4)
G: famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent)


## Features Used to Train the Model





## Deployment Instructions

### For Users
From the dockerfile directory, run:

    docker build -t ml:latest .
    docker run -d -p 5000:5000 ml
    curl http://localhost:5000/predict

And navigate to http://localhost:5000/predict within your web browser.

### For Developers
To make changes to the ML microservice, edit the model as needed in model_build.ipynb, and the API as needed in dockerfile/apps/app.py. 

To integrate the new model with the Flask API, run the following cell in model_build.ipynb:

    import joblib
    # modify the file path to where you want to save the model
    joblib.dump(clf, 'home/matrix/dockerfile/apps/model.pkl')

## Tests 
We have set up a Github Actions workflow that uses pytest to test our API.
