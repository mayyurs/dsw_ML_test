# -*- coding: utf-8 -*-
"""model_random_forest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/170x7tgGUx3O06lO_WIKquPIqkOnagJlD

Random Forest is an ensemble learning method that combines the predictions of multiple individual decision trees to make more accurate predictions. Each decision tree in the forest is trained on a random subset of the training data and makes independent predictions.
"""

# model_random_forest.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Object-oriented, class-based approach :
class RandomForestModel:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.label_encoders = {}

# loading function
def load(self, data_file):
        self.data = pd.read_csv(data_file)

# pre-processing function
def preprocess(self):
        self.data.fillna(method='ffill', inplace=True)
        for col in ['category', 'main_promotion', 'color']:
            self.label_encoders[col] = LabelEncoder()
            self.data[col] = self.label_encoders[col].fit_transform(self.data[col])
        self.X = self.data.drop(columns=['item_no', 'success_indicator'])
        self.y = self.data['success_indicator']

# training function
def train(self):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)
        self.model.fit(self.X_train, self.y_train)

# testing function
def test(self):
        y_pred = self.model.predict(self.X_test)
        print("Accuracy:", accuracy_score(self.y_test, y_pred))
        print("Classification Report:")
        print(classification_report(self.y_test, y_pred))

# predicting function
def predict(self, input_data_file):
        input_data = pd.read_csv(input_data_file)
        input_data.fillna(method='ffill', inplace=True)
        for col in ['category', 'main_promotion', 'color']:
            input_data[col] = self.label_encoders[col].transform(input_data[col])
        predictions = self.model.predict(input_data.drop(columns=['item_no']))
        return predictions