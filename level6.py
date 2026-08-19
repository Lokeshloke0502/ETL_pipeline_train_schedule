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

# 4 Feature Engineering 

# Convert distance to numeric
model_df["distance"] = pd.to_numeric(
    model_df["distance"],
    errors="coerce")

# Convert time fields
arrival = pd.to_datetime(
    model_df["arrival_time"],
    format="%H:%M:%S",
    errors="coerce")

departure = pd.to_datetime(
    model_df["departure_time"],
    format="%H:%M:%S",
    errors="coerce")

# Extract time-based features
model_df["arrival_hour"] = arrival.dt.hour

model_df["departure_hour"] = departure.dt.hour

# 5 Select Features 

FEATURES = [
    "distance",
    "arrival_hour",
    "departure_hour"]

model_df = model_df[
    FEATURES + [TARGET]
].dropna()

X = model_df[FEATURES]
y = model_df[TARGET]


print("\nSelected Features:")
print(FEATURES)

print(f"\nFinal modelling records: {len(model_df):,}")

# 6 Train / Test split 

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining samples:", f"{len(X_train):,}")
print("Testing samples :", f"{len(X_test):,}")