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

To train the model in an ideal way, we must understand the nature of what problem we are trying to solve.
For this project, we are trying to determine how to predict if a student is a "quality" student or not - 
a quality student meaning they have a G3 score of 15 or greater.

Per the handout, "student performance is described by their grades (G1, G2, G3), where G3 is the final year
grade". This means that G1, G2, and G3 should not be part of the features used to train the model. Why?
Because we are trying to **predict** if a student will be quality, we shouldn't use information when the 
student is already accepted (G1, G2, G3), since that is self-defeating.

That being said, we have chosen certain features that we believe will be indicators of a quality student.
These features and the reasons why are listed below:

1. Studytime: The weekly study time for a student is an indicator of diligence and good school habits.
              Even though the student will be going to a different school, study habits are an important
              part of potential success and it is a transferable skill.
              
2. Absences:  The number of school absences in general (i.e. being very smart, illness, family emergency, 
              etc.) are a good indicator for a quality student. A quality student generally attends 
              school and class on a consistent basis (if you are very smart, it is possbile to still be a
              quality student and miss class).
              
3. Age:       While age certainly does not determine intelligence, someone with more years of experience
              in school generally will have more knowledge and have gone through the rigor of school over
              a longer period of time than someone younger.
              
4. Health:    Someone with poor health status could potentially negatively affect their performance in school
              depending on how serious the health condition is.
              
5. Goout:     People who hang out with friends for a moderate to low amount probably have a better chance
              to have higher grades - since they can focus more time on studying and doing homework. Of 
              course, there are cases where a student can be very productive, have excellent time management
              skills, hang out with friends a lot, and do well in school. For the majority though, it is
              reasonable that less time hanging out with friends will probably correlate to more time in
              school.
              
6. Failures:  The number of past class failures shows history for a student's school habits. A student can
              change, but there is evidence for potentially bad habits if their history is bad.

7. Famrel:    This is debatable, but the better the family relations, probably less stress on a person's life,
              which is definitely helpful to someone's school life, as school can be very stressful already.

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
