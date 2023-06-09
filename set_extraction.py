# -*- coding: utf-8 -*-
"""set_extraction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12wuVmBjqfv5XRWVePY1KQLFbjTdfG99m

# Libraries
"""



import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

"""# Data Loading

"""

cols = ["ID", "INPUT0", "INPUT1", "INPUT2", "INPUT3", "INPUT4", "INPUT5", "INPUT6", "INPUT7", "INPUT8", "TARGET_X", "TARGET_Y"]

dtf = pd.read_csv('data/ML-CUP22-TR.csv', skiprows=7, header=None, sep=",", names=cols)

dtf.head(3)

dtf.set_index("ID", inplace=True)

dtf.shape

dtf.info()

"""# Check for correlations

"""

dtf.corr()

fig, ax = plt.subplots(figsize=(10,10))         
sns.heatmap(dtf.corr(), annot=True)
plt.show()

"""# Development Set (80%) and Test Set (20%) Extraction

"""

x = dtf.iloc[:,0:9]    
y = dtf.iloc[:,9:11]

x.head()

y.head()

# data normalization

scaler = StandardScaler()

cols = x.columns
x = pd.DataFrame(scaler.fit_transform(x.values), columns=cols)  # now x values are scaled (not targets)

x.head()

y.head()

x_arr = x.to_numpy().astype(np.float64)
y_arr = y.to_numpy().astype(np.float64)

x_train, x_test, y_train, y_test = train_test_split(x_arr, y_arr, test_size=0.3, random_state=42, shuffle=True)



print("x_train ", x_train.shape)
print("y_train ", y_train.shape)
print("x_test ", x_test.shape)
print("y_test ", y_test.shape)