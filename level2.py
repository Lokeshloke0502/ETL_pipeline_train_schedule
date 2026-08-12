# Task 2.1: Identify and handle missing values
import pandas as pd
df = pd.read_csv("Dataset1_intern.csv")
# 2.1.1 Standardize the column name

df.rename(columns={"SN":"sn","Train_No":"train_number","Station_Code":"station_code","Station_Name":"station_name",
                   "1A":"first_ac", "2A":"second_ac","3A":"third_ac", "Route_Number":"route_number",
                   "SL": "sleeper","Arrival_time":"arrival_time","Departure_Time":"departure_time","Distance":"distance"}, inplace=True)

print(df.columns.tolist()) 

# 2.1.2 Fix the serial number 
df["sn"] = range(1, len(df) + 1)

print(df.head(10))

# 2.1.3