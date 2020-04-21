import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys, os, scipy, sklearn
import sklearn.metrics, sklearn.preprocessing, sklearn.model_selection, sklearn.tree, sklearn.linear_model, sklearn.cluster

mpl.rcParams['font.size'] = 14
pd.options.display.max_columns = 1000

#import data sets
wbc = pd.read_csv('/Users/vaibhav/Desktop/Python Projects/DataCamp-Data Scientist with python/25-Machine Learning with Tree-Based Models in Python/wbc.csv')
indian_liver_patient = pd.read_csv('/Users/vaibhav/Desktop/Python Projects/DataCamp-Data Scientist with python/25-Machine Learning with Tree-Based Models in Python/indian_liver_patient.csv')
indian_liver_patient_preprocessed = pd.read_csv('/Users/vaibhav/Desktop/Python Projects/DataCamp-Data Scientist with python/25-Machine Learning with Tree-Based Models in Python/indian_liver_patient_preprocessed.csv')
bikes = pd.read_csv('/Users/vaibhav/Desktop/Python Projects/DataCamp-Data Scientist with python/25-Machine Learning with Tree-Based Models in Python/bikes.csv')
auto = pd.read_csv('/Users/vaibhav/Desktop/Python Projects/DataCamp-Data Scientist with python/25-Machine Learning with Tree-Based Models in Python/auto.csv')

df = wbc

label_encoder = sklearn.preprocessing.LabelEncoder()
label_encoder.fit(df['diagnosis'])

X= df[['radius_mean', 'concave points_mean']]
y = label_encoder.transform(df['diagnosis'])

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X,y)

SEED = 1
