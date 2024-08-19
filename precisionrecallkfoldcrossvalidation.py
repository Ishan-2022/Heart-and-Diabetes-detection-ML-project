# -*- coding: utf-8 -*-
"""PrecisionRecallKFoldCrossValidation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1boMouC6XV7P4-WYesG5wGjr2JkYOp1L7
"""

import pandas as pd
from google.colab import files
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import precision_score, recall_score
from sklearn.svm import SVC

uploaded = files.upload()

data = pd.read_csv("diabetes.csv")

data.head()

X = data.drop("Outcome", axis=1)
y = data["Outcome"]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
model = SVC(kernel='linear',C=1.0,random_state=42)
model.fit(X_train,y_train)
patient_data = {
    "Pregnancies": None,
    "Glucose": None,
    "BloodPressure": None,
    "SkinThickness": None,
    "Insulin": None,
    "BMI": None,
    "DiabetesPedigreeFunction": None,
    "Age": None
}
for feature in patient_data:
  patient_data[feature] = float(input("Enter {} for the patient:".format(feature)))

patient_df = pd.DataFrame(patient_data, index=[0])
prediction = model.predict(patient_df)
print("\nPatient Data:")
print(patient_df)
if prediction[0] == 1:
  print("Diabetes Detected")
else:
  print("Normal")

def model_evaluation(data):
  X = data.drop("Outcome", axis=1)
  y = data["Outcome"]
  model = SVC(kernel='linear',C=1.0,random_state=42)
  cv_score = cross_val_score(model, X, y, cv=5)
  cv_prediction = cross_val_predict(model, X, y, cv=5)
  cv_accuracy = cv_score.mean()
  cv_precision = precision_score(y, cv_prediction)
  cv_recall = recall_score(y, cv_prediction)
  print("Cross Validated Accuracy:",cv_accuracy)
  print("Cross Validated Precision:",cv_precision)
  print("Cross Validated Recall:",cv_recall)
data = pd.read_csv("diabetes.csv")
model_evaluation(data)