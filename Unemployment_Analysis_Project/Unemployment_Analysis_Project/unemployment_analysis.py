import pandas as pd
import matplotlib.pyplot as plt

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