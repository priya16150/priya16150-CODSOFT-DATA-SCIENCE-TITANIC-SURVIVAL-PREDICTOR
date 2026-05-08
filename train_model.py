import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

df = pd.read_csv('titanic.csv')

features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
df_model = df[features + ['Survived']].copy()

df_model = df_model.dropna(subset=['Embarked'])

df_model['Age'].fillna(df_model['Age'].median(), inplace=True)

le_sex = LabelEncoder()
le_embarked = LabelEncoder()
df_model['Sex'] = le_sex.fit_transform(df_model['Sex'])      # male=1, female=0
df_model['Embarked'] = le_embarked.fit_transform(df_model['Embarked'])  # S=2, C=0, Q=1

X = df_model[features]
y = df_model['Survived']

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, 'titanic_model.pkl')
joblib.dump(le_sex, 'le_sex.pkl')
joblib.dump(le_embarked, 'le_embarked.pkl')

print("✅ Model training complete. Saved as 'titanic_model.pkl'")