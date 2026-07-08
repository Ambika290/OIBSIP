#Loading the dataset
import pandas as pd

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())



#cleaning the dataset
import pandas as pd

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove Missing Values
df = df.dropna()

print("Dataset Shape After Cleaning:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())



#Graph 1: Unemployment Rate Distribution
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove Missing Values
df = df.dropna()

# Histogram
plt.hist(df[' Estimated Unemployment Rate (%)'])

plt.title("Unemployment Rate Distribution")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")

plt.show()



#Graph 2: Average Unemployment Rate by Region
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove Missing Values
df = df.dropna()

# Average unemployment rate by region
region_data = df.groupby('Region')[' Estimated Unemployment Rate (%)'].mean()

# Bar Chart
region_data.sort_values(ascending=False).plot(kind='bar', figsize=(12,6))

plt.title("Average Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Average Unemployment Rate (%)")

plt.tight_layout()
plt.show()

import pandas as pd
import matplotlib.pyplot as plt


#Next Graph: Urban vs Rural Unemployment
# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Remove Missing Values
df = df.dropna()

# Average unemployment by area
area_data = df.groupby('Area')[' Estimated Unemployment Rate (%)'].mean()

# Pie Chart
plt.pie(
    area_data,
    labels=area_data.index,
    autopct='%1.1f%%'
)

plt.title("Urban vs Rural Unemployment Rate")
plt.show()
