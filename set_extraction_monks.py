# -*- coding: utf-8 -*-
"""set_extraction_monks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1c4BJyGQ_G3V5wZ4dKvTGOutN2fzMWgNc

# Libraries
"""



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder
from sklearn.utils import shuffle

"""# Data Loading monks-1

"""

cols = ['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'Id']

train_m1 = pd.read_csv("data/monks-1.train", sep = " ", skipinitialspace=True, names = cols)

test_m1 = pd.read_csv("data/monks-1.test", sep = " ", skipinitialspace=True, names = cols)

train_m1.head(3)

test_m1.head(3)

train_m1.set_index("Id", inplace=True)
test_m1.set_index("Id", inplace=True)

train_m1.head(3)

test_m1.head(3)

train_m1.shape

test_m1.shape

train_m1.info()

test_m1.info()

x_train_m1 = train_m1.iloc[:, 1:7].values
y_train_m1 = train_m1.iloc[:, 0].values

x_test_m1 = test_m1.iloc[:, 1:7].values
y_test_m1 = test_m1.iloc[:, 0].values

print("Shapes before encoding:")
print("x_train_m1", x_train_m1.shape)
print("y_train_m1", y_train_m1.shape)
print("x_test_m1", x_test_m1.shape)
print("y_test_m1", y_test_m1.shape)

# Encoding
encoder = OneHotEncoder(sparse=False)
x_train_m1 = encoder.fit_transform(x_train_m1)

encoder = OneHotEncoder(sparse=False)
x_test_m1 = encoder.fit_transform(x_test_m1)

x_train_m1, y_train_m1 = shuffle(x_train_m1, y_train_m1, random_state=42)
x_test_m1, y_test_m1 = shuffle(x_test_m1, y_test_m1, random_state=42)

print("Shapes after encoding:")
print("x_train_m1", x_train_m1.shape)
print("y_train_m1", y_train_m1.shape)
print("x_test_m1", x_test_m1.shape)
print("y_test_m1", y_test_m1.shape)

"""# Data Loading monks-2

"""

cols = ['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'Id']

train_m2 = pd.read_csv("data/monks-2.train", sep = " ", skipinitialspace=True, names = cols)

test_m2 = pd.read_csv("data/monks-2.test", sep = " ", skipinitialspace=True, names = cols)

train_m2.head(3)

test_m2.head(3)

train_m2.set_index("Id", inplace=True)
test_m2.set_index("Id", inplace=True)

train_m2.head(3)

test_m2.head(3)

train_m2.shape

test_m2.shape

train_m2.info()

test_m2.info()

x_train_m2 = train_m2.iloc[:, 1:7].values
y_train_m2 = train_m2.iloc[:, 0].values

x_test_m2 = test_m2.iloc[:, 1:7].values
y_test_m2 = test_m2.iloc[:, 0].values

print("Shapes before encoding:")
print("x_train_m2", x_train_m2.shape)
print("y_train_m2", y_train_m2.shape)
print("x_test_m2", x_test_m2.shape)
print("y_test_m2", y_test_m2.shape)

# Encoding
encoder = OneHotEncoder(sparse=False)
x_train_m2 = encoder.fit_transform(x_train_m2)

encoder = OneHotEncoder(sparse=False)
x_test_m2 = encoder.fit_transform(x_test_m2)

x_train_m2, y_train_m2 = shuffle(x_train_m2, y_train_m2, random_state=42)
x_test_m2, y_test_m2 = shuffle(x_test_m2, y_test_m2, random_state=42)

print("Shapes after encoding:")
print("x_train_m2", x_train_m2.shape)
print("y_train_m2", y_train_m2.shape)
print("x_test_m2", x_test_m2.shape)
print("y_test_m2", y_test_m2.shape)

"""# Data Loading monks-3

"""

cols = ['class', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'Id']

train_m3 = pd.read_csv("data/monks-3.train", sep = " ", skipinitialspace=True, names = cols)

test_m3 = pd.read_csv("data/monks-3.test", sep = " ", skipinitialspace=True, names = cols)

train_m3.head(3)

test_m3.head(3)

train_m3.set_index("Id", inplace=True)
test_m3.set_index("Id", inplace=True)

train_m3.head(3)

test_m3.head(3)

train_m3.shape

test_m3.shape

train_m3.info()

test_m3.info()

x_train_m3 = train_m3.iloc[:, 1:7].values
y_train_m3 = train_m3.iloc[:, 0].values

x_test_m3 = test_m3.iloc[:, 1:7].values
y_test_m3 = test_m3.iloc[:, 0].values

print("Shapes before encoding:")
print("x_train_m3", x_train_m3.shape)
print("y_train_m3", y_train_m3.shape)
print("x_test_m3", x_test_m3.shape)
print("y_test_m3", y_test_m3.shape)

# Encoding
encoder = OneHotEncoder(sparse=False)
x_train_m3 = encoder.fit_transform(x_train_m3)

encoder = OneHotEncoder(sparse=False)
x_test_m3 = encoder.fit_transform(x_test_m3)

x_train_m3, y_train_m3 = shuffle(x_train_m3, y_train_m3, random_state=42)
x_test_m3, y_test_m3 = shuffle(x_test_m3, y_test_m3, random_state=42)

print("Shapes after encoding:")
print("x_train_m3", x_train_m3.shape)
print("y_train_m3", y_train_m3.shape)
print("x_test_m3", x_test_m3.shape)
print("y_test_m3", y_test_m3.shape)