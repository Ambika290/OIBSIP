import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("Advertising.csv")

plt.scatter(df['TV'], df["Sales"])

plt.title("TV Advertising vs Sales") 
plt.xlabel("TV Advertising") 
plt.ylabel("Sales")

plt.show()