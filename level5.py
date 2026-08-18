import pandas as pd
import matplotlib.pyplot as plt

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
    top_distance["total_distance"]
)

plt.xlabel("Train Number")
plt.ylabel("Total Distance")
plt.title("Top 20 Trains by Total Distance")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()