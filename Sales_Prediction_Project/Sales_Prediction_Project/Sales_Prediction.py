import pandas as pd

# Load dataset
df = pd.read_csv("Advertising.csv")

# Display first 5 rows
print(df.head())



import pandas as pd

# Load dataset
df = pd.read_csv("Advertising.csv")

# Show first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset information
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())




import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Advertising.csv")

# Histogram of Sales
plt.hist(df['Sales'])

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.show()






import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("Advertising.csv")

plt.scatter(df['TV'], df["Sales"])

plt.title("TV Advertising vs Sales") 
plt.xlabel("TV Advertising") 
plt.ylabel("Sales")

plt.show()





import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("Advertising.csv")

# Remove unnecessary column
df.drop("Unnamed: 0", axis=1, inplace=True)

# Features and Target
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
score = r2_score(y_test, y_pred)

print("R2 Score:", score)
