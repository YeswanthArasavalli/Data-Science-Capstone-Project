# -*- coding: utf-8 -*-
"""env.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OMOKTnyVCk-5zVMtXVE3G5vOYeWQNQvW
"""

import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder  # Import LabelEncoder
import matplotlib.pyplot as plt  # Import Matplotlib for plots
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the dataset (assuming 'car_details.csv' is in your app directory)
df = pd.read_csv('car_details.csv')

# Explore the dataset
st.write(df.head())
st.write(df.info())

# Handle missing values (you can customize this based on your data)
st.write(df.isnull().sum())
# You can choose to fill missing values, drop rows, or implement a strategy here
# ...

# Encode categorical variables
le = LabelEncoder()
df['fuel'] = le.fit_transform(df['fuel'])
df['seller_type'] = le.fit_transform(df['seller_type'])
df['transmission'] = le.fit_transform(df['transmission'])
df['owner'] = le.fit_transform(df['owner'])

# Exploratory Data Analysis
# Visualize the distribution of numerical features
st.write("Distribution of Car Year")

# Use Matplotlib to create the histogram
fig, ax = plt.subplots()
ax.hist(df['year'])
st.pyplot(fig)  # Display the Matplotlib figure in Streamlit

st.write("Distribution of Selling Price")
fig, ax = plt.subplots()
ax.hist(df['selling_price'])
st.pyplot(fig)

st.write("Distribution of Kilometers Driven")
fig, ax = plt.subplots()
ax.hist(df['km_driven'])
st.pyplot(fig)

# Analyze the relationships between features
st.write("Correlation Matrix")

# Calculate correlation on numerical columns only
numerical_df = df.select_dtypes(include=['number'])
st.write(numerical_df.corr())

# Prepare the data for machine learning
X = df.drop(['name','selling_price'], axis=1)  # Remove 'name' as a feature
y = df['selling_price']  # Predict 'selling_price'

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and evaluate machine learning models
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_mse = mean_squared_error(y_test, lr_pred)
lr_r2 = r2_score(y_test, lr_pred)

rf = RandomForestRegressor()
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_mse = mean_squared_error(y_test, rf_pred)
rf_r2 = r2_score(y_test, rf_pred)

# Determine the best model based on the evaluation metrics (add logic here)

# You don't need to save the model in the deployment script
# This section is for illustration only (remove for deployment)
# import pickle
# pickle.dump(best_model, open('car_details_model.pkl', 'wb'))

# Load the saved model (remove for deployment)
# loaded_model = pickle.load(open('car_details_model.pkl', 'rb'))