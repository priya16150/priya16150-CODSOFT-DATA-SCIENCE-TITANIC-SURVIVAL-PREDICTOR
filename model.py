import joblib
import numpy as np

model = joblib.load('titanic_model.pkl')
le_sex = joblib.load('le_sex.pkl')
le_embarked = joblib.load('le_embarked.pkl')

def predict_survival(pclass, sex, age, sibsp, parch, fare, embarked):
    """
    Predict survival for a single passenger.
    Returns (prediction, probability)
    """
    sex_encoded = le_sex.transform([sex])[0]
    embarked_encoded = le_embarked.transform([embarked])[0]
    
    features = np.array([[pclass, sex_encoded, age, sibsp, parch, fare, embarked_encoded]])
    
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]  
    
    return int(prediction), float(probability)
