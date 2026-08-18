import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)

# Task 5.1.1 Create charts to visualize train stops

train_stops = pd.read_csv("train_stops.csv")

train_distance = pd.read_csv("train_distance.csv")

top_stops = train_stops.sort_values(
    "number_of_stops",
    ascending=False).head(20)

plt.figure(figsize=(12, 6))

plt.bar(
    top_stops["train_number"].astype(str),
    top_stops["number_of_stops"]
)

plt.xlabel("Train Number")
plt.ylabel("Number of Stops")
plt.title("Top 20 Trains by Number of Stops")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Task 5.1.2 Create charts to visualize total distance

top_distance = train_distance.sort_values(
    "total_distance_traveled",
    ascending=False
).head(20)

plt.figure(figsize=(12, 6))

plt.bar(
    top_distance["train_number"].astype(str),
    top_distance["total_distance_traveled"]
)

plt.xlabel("Train Number")
plt.ylabel("Total Distance")
plt.title("Top 20 Trains by Total Distance")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Task 5.2: Visualize the distribution of journey duration

df = pd.read_csv("train_reporting_dataset.csv")

# drop Nan values 

duration = df["journey_duration_minutes"].dropna()

# create histogram

plt.figure(figsize=(10,6))
plt.hist("duration",bins=30)
plt.xlabel("Journey Duration (minutes)")
plt.ylabel("Number of Records")
plt.title("Distribution of Journey Duration")

plt.tight_layout()
plt.show()

print(duration.describe())

#Task 5.3: Split the dataset into training and testing subsets

model_df = df[["distance","journey_duration_minutes"]].dropna()

x = model_df[["distance"]]
y= model_df[["journey_duration_minutes"]]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=42)

print("Training records:", len(x_train))
print("Testing records:", len(x_test))


# Task 5.4: Build a simple predictive model to estimate journey duration

# create model

model = LinearRegression()

# train model
model.fit(x_train,y_train)

# predict model

y_pred = model.predict(x_test)

# evaluate the model

mae = mean_absolute_error(y_test,y_pred)

rmse = mean_squared_error(y_test,y_pred) ** 0.5

r2 = r2_score(y_test,y_pred)

print("MAE:", mae)
print("RMSE:", rmse)
print("R² Score:", r2)