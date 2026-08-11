import pandas as pd

# Task 1.1 Load the train schedule dataset
df = pd.read_csv("Dataset1_intern.csv")


# Task 1.2 Verifying records and attributes
print("Dataset Shape:", df.shape)
print("Total Records:", df.shape[0])
print("Total Attributes:", df.shape[1])

# 1.3.1 Review column names
print("\nColumn Names:")
print(df.columns.tolist())


# 1.3.1 Review data types
print("\nData Types:")
print(df.dtypes)


# 1.4 Preserve raw dataset
raw_df = df.copy()
raw_df.to_csv("DataBackup.csv",index=False)


# Complete information
print("\nDataset Information:")
print(df.info())