import pandas as pd
df = pd.read_csv(r":\Users\hp\Desktop\Titanic-Dataset.csv")

# Dataset dimensions
print("Shape:")
df.shape

# Column names and data types
print("\nColumns:")
df.columns
print("\nData Types:")
df.dtypes

# Statistic summary
print("\nStatistical Summary:")
df.describe()

# Display the first five rows
print("First five rows:")
print(df.head())

# Display the last five rows
print("Last five rows:")
print(df.tail())

# Display dataset information
print("\nDataset information")
df.info()

# Display passenger names
print("\nPassenger names")
print(df["Name"].head())

# Count passenger by class
print("\nPassengers by Gender:")
print(df["Pclass"].value_counts())

# Calculate average age
print("\nAverage age:")
print(df["Age"].mean())

# Find the highest fare
print("\nHighest fare")
print(df["Fare"].max())

# Dropping a column
df.drop(["Cabin","Embarked"],axis=1)

# Filter passengers older than 60
print("\nPassengers older than 60:")
print(df[df["Age"]>60])

# Display passengers who survived
print("\nPassengers who survived:")
print(df[df["Survived"]==1][["Name","Sex","Age"]].head())

# Display Survival names
print("\nSurvival Counts:")
print(df["Survived"].value_counts())

# Display survival names by gender
print("\nSurvival Rate by Gender:")
print(df.groupby("Sex")["Survived"].mean())

# Display the highest fare
print("\nTop 10 Highest Fares:")
print(
    df.sort_values("Fare",ascending=False)
    [["Name","Fare"]]
    .head(10)
)
    
# Count passengers by 
print("\nPassengers by Class:")
print(df["Pclass"].value_counts().sort_index())

# Displaying gender by age
print("\nAverage Age by Gender:")
print(df.groupby("Sex")["Age"].mean())

# Display embarkation port counts
print("\nPassengers by Embarkation port:")
print(df["Embarked"].value_counts())

# Save a copy of the dataset 
df.to_csv(".csv",index=False)

# Handling missing values
for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtypes(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else: 
            df[col] = df[col].fillna(df[col].mode() [0])
print("\nMissing values handled")
