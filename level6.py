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

# Load Dataset

DATA_PATH = "train_reporting_dataset.csv"

df = pd.read_csv(DATA_PATH)

print()
print("DATASET INFORMATION")
print()

print(f"Rows    : {df.shape[0]:,}")
print(f"Columns : {df.shape[1]:,}")