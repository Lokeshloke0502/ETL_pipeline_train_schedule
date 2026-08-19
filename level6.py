import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# 1 Load Dataset

DATA_PATH = "train_reporting_dataset.csv"

df = pd.read_csv(DATA_PATH)

print()
print("DATASET INFORMATION")
print()

print(f"Rows    : {df.shape[0]:,}")
print(f"Columns : {df.shape[1]:,}")

# 2 Data Quality check

print("\nMissing Values:")
print(df.isnull().sum())

print(
    "\nDuplicate Records:",
    df.duplicated().sum()
)

# 3 Define Target 

TARGET = "journey_duration_minutes"

model_df = df.dropna(subset=[TARGET]).copy()


# 5 Select Features 

FEATURES = [
    "distance"]

model_df = model_df[
    FEATURES + [TARGET]
].dropna()

X = model_df[FEATURES]
y = model_df[[TARGET]]


print("\nSelected Features:")
print(FEATURES)

print(f"\nFinal modelling records: {len(model_df):,}")

# 6 Train / Test split 

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20,random_state=42)

print("\nTraining samples:", f"{len(X_train):,}")
print("Testing samples :", f"{len(X_test):,}")

# 7 Create Decision Tree 

model = DecisionTreeRegressor(
    criterion="squared_error",
    max_depth=10,
    min_samples_split=20,
    min_samples_leaf=10,
    random_state=42
)

# 8 Train the Model

model.fit(
    X_train,
    y_train
)

print("\nDecision Tree training completed.")

# 9 Predictions

y_train_pred = model.predict(X_train)

y_test_pred = model.predict(X_test)