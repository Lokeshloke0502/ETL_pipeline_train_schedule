import pandas as pd

df = pd.read_csv("train_reporting_dataset.csv")

print(df.shape)

# 4.1 Generate a train-level table showing number of stops

train_stops = (df.groupby("train_number").agg(number_of_stops = ("station_code","count")).reset_index())

print(train_stops.head())

# 4.2 Generate a train-level table showing total distance

train_distance = (df.groupby("train_number").agg(total_distance_traveled = ("distance","max")).reset_index())

print(train_distance.head())

# 4.3: Create a cross table comparing trains and stations

train_station_cross_table = pd.crosstab(df["train_number"],df["station_name"])

print(train_station_cross_table.head())

# 4.4: Export all structured tables for reporting 


train_stops.to_csv("train_stops.csv",index = False)

train_distance.to_csv("train_distance.csv",index = False)
