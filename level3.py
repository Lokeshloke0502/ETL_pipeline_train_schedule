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

# 3.2 Derive a new feature representing journey duration

df = df.sort_values(
    ["train_number", "route_number"]
).reset_index(drop=True)

# To find the next stations arrival time

df["next_arrival_time"] = (
    df.groupby("train_number")["arrival_time"]
      .shift(-1)
)

# Then calculating the duration 

df["journey_duration"] = (
    df["next_arrival_time"] - df["departure_time"]
)

# Handle midnight crossing 

df.loc[
    df["journey_duration"] < pd.Timedelta(0),
    "journey_duration"
] += pd.Timedelta(days=1)


# Convert it into minutes 

df["journey_duration_minutes"] = (
    df["journey_duration"]
    .dt.total_seconds() / 60
)

df.head()
