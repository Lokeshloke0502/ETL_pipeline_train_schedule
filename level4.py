import pandas as pd

df = pd.read_csv("Validate_dataset.csv")

print(df.shape)

# Generate a train-level table showing number of stops

train_stops = (df.groupby("train_number").agg(number_of_stops = ("station_code","count")).reset_index())

print(train_stops.head())

# Generate a train-level table showing total distance

train_distance = (df.groupby("train_number").agg(total_distance_traveled = ("distance","max")).reset_index())

print(train_distance.head())