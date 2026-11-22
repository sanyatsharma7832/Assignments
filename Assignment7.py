import pandas as pd
df=pd.read_csv(r"C:\Users\hp\Desktop\Titanic-Dataset.csv")
import matplotlib.pyplot as plt

# Count passengers in each class
counts = df["Pclass"].value_counts().sort_index()

# BAR GRAPH
plt.bar(counts.index,counts.values)

counts = df.groupby(["Survived","Sex"]).size().unstack()
print(counts)
counts.plot(kind="bar")

plt.xlabel("Survival status")
plt.ylabel("Number of passengers")
plt.title("Titanic survival by Gender")

plt.xticks([0,1],["Not survived","Survived"],rotation=0)
plt.show()

# SCATTERPLOT
data= df.dropna(subset=["Age","Fare"])
plt.scatter(data["Age"],data["Fare"])

# Add label and title
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title("Age vs Fare in CSV dataset")
plt.grid(True)

# Calculate average fare for each class
avg_fare= df.groupby("Pclass")["Fare"].mean()

# LINE GRAPH
plt.plot(avg_fare.index, avg_fare.values, marker="o")

# Add labels and title
plt.xlabel("Passenger class")
plt.ylabel("Average Fare")
plt.title("Average Fare by passenger class")

plt.xticks([1,2,3])
plt.grid(True)
plt.show()

