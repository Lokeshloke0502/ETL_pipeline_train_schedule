import pandas as pd 

df = pd.read_csv("Validate_dataset.csv")

# Task 3.1 Convert time-based fields into datetime format
df["arrival_time"] = pd.to_datetime(
    df["arrival_time"],
    format="%H:%M:%S")

df["departure_time"] = pd.to_datetime(
    df["departure_time"],
    format="%H:%M:%S")


print(df[["arrival_time", "departure_time"]].dtypes)

