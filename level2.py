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

# 2.1.3 Remove unwanted special character

df["station_name"] = (
    df["station_name"]
    .astype("string")
    .str.upper()
    .str.replace(r"[^A-Z0-9]+", " ", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)

print(df.head(40))


# 2.1.4 Identify
print(df.isnull().sum())

# 2.1.5 View missing rows
print(df[df.isnull().any(axis=1)])

# 2.1.6 Handle only confirmed problematic records
df = df.dropna(subset=["station_name"])

# 2.1.7 Verify
print("Remaining rows:", len(df))
print(df.isnull().sum())



# 2.2.1 Display duplicate records
print(df[df.duplicated(keep=False)])

# 2.2.2 Remove duplicates
df = df.drop_duplicates()

# 2.2.3Check final row count
print("Rows after removing duplicates:", len(df))

# 2.2.4 Verify
print("Duplicates remaining:", df.duplicated().sum())


# 2.3.1 Convert text to time
time_columns = ["arrival_time", "departure_time"]

for column in time_columns:
    df[column] = pd.to_datetime(
        df[column].astype(str).str.strip(),
        format="%H:%M:%S",
        errors="coerce"
    )


#2.3.2 Check invalid values
for column in time_columns:
    print(
        column,
        "invalid values:",
        df[column].isna().sum()
    )

# 2.3.3 Standardize the time format
for column in time_columns:
    df[column] = df[column].dt.strftime("%H:%M:%S")
print(df[["arrival_time", "departure_time"]].head(10))
