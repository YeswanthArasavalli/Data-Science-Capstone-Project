# -*- coding: utf-8 -*-
"""Untitled5_py.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GwarxRhCiARvfsptVUV7eEEBO_oDkBdz
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a=pd.read_csv('CAR DETAILS.csv')
a.head(5)

# Check for missing values
print(a.isnull().sum())

# Remove duplicates
a.drop_duplicates(inplace=True)

# Display the cleaned dataset
print(a.head(5))

a['name'].fillna(a['name'].mode()[0], inplace=True)

# One-Hot Encoding (for categorical features)
# Assuming 'fuel_type' is a categorical feature
a = pd.get_dummies(a, columns=['fuel'])

# Imputation (for numerical features)
a['year'].fillna(a['year'].mean(), inplace=True)

# Scaling of Data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# Assuming 'selling_price' is a numerical feature you want to scale
a[['selling_price']] = scaler.fit_transform(a[['selling_price']])

# Display the pre-processed dataset
print(a.head(5))

# Summary statistics
print(a.describe())

# Correlation matrix
corr_matrix = a.corr(numeric_only=True)
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Histograms for numerical features
a.hist(figsize=(12, 10), bins=20)
plt.show()

# Box plots for numerical features
a.boxplot(figsize=(12, 10))
plt.show()

# Scatter plots for relationships between features
plt.figure(figsize=(8, 6))
sns.scatterplot(x='year', y='selling_price', data=a)
plt.title('Year vs Selling Price')
plt.show()

# Pairplot for visualizing relationships between multiple features
sns.pairplot(a[['selling_price', 'km_driven', 'year']])
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, BaggingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Separate features (X) and target variable (y)
X = a.drop(['selling_price', 'name', 'seller_type', 'owner'], axis=1) # Dropping the 'owner' column
y = a['selling_price']

X = pd.get_dummies(X, columns=['transmission'])
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)
lr_mse = mean_squared_error(y_test, lr_predictions)
lr_r2 = r2_score(y_test, lr_predictions)
print(f"Linear Regression - MSE: {lr_mse}, R-squared: {lr_r2}")

# Random Forest Regression
rf_model = RandomForestRegressor(random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)
rf_mse = mean_squared_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)
print(f"Random Forest Regression - MSE: {rf_mse}, R-squared: {rf_r2}")

# Gradient Boosting Regression
gb_model = GradientBoostingRegressor(random_state=42)
gb_model.fit(X_train, y_train)
gb_predictions = gb_model.predict(X_test)
gb_mse = mean_squared_error(y_test, gb_predictions)
gb_r2 = r2_score(y_test, gb_predictions)
print(f"Gradient Boosting Regression - MSE: {gb_mse}, R-squared: {gb_r2}")

# Bagging Regression
bagging_model = BaggingRegressor(random_state=42)
bagging_model.fit(X_train, y_train)
bagging_predictions = bagging_model.predict(X_test)
bagging_mse = mean_squared_error(y_test, bagging_predictions)
bagging_r2 = r2_score(y_test, bagging_predictions)
print(f"Bagging Regression - MSE: {bagging_mse}, R-squared: {bagging_r2}")

import pickle

# Save the best model (e.g., Random Forest)
best_model = rf_model  # Replace with the actual best model
filename = 'best_model.sav'
pickle.dump(best_model, open(filename, 'wb'))

# Load the saved model
loaded_model = pickle.load(open(filename, 'rb'))

# Use the loaded model for predictions
predictions = loaded_model.predict(X_test)

# picking 20 data points from the CAR DETAILS dataset and apply
# the saved model on the same Dataset and test the model.
# Sample 20 random data points
sample_data = a.sample(n=20, random_state=42)

# Separate features (X) and target variable (y) for the sample data
X_sample = sample_data.drop(['selling_price', 'name', 'seller_type', 'owner'], axis=1)
y_sample = sample_data['selling_price']

# One-hot encode the categorical features in the sample data
X_sample = pd.get_dummies(X_sample, columns=['transmission'])

# Use the loaded model for predictions on the sample data
sample_predictions = loaded_model.predict(X_sample)

# Evaluate the model on the sample data
sample_mse = mean_squared_error(y_sample, sample_predictions)
sample_r2 = r2_score(y_sample, sample_predictions)
print(f"Sample Data - MSE: {sample_mse}, R-squared: {sample_r2}")