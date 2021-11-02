# Team Name HW4

## API instructions:




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
