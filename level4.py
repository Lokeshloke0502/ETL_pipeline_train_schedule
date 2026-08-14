import pandas as pd

df = pd.read_csv("Validate_dataset.csv")

print(df.shape)

# 4.1 Generate a train-level table showing number of stops

train_stops = (df.groupby("train_number").agg(number_of_stops = ("station_code","count")).reset_index())

print(train_stops.head())

# 4.2 Generate a train-level table showing total distance

train_distances = (df.groupby("train_number").agg(total_distance_traveled = ("distance","max")).reset_index())

print(train_distances.head())

# 4.3: Create a cross table comparing trains and stations

train_station_cross_table = pd.crosstab(df["train_number"],df["station_name"])

print(train_station_cross_table.head())