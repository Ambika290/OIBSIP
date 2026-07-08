import pandas as pd

# Load Dataset
df = pd.read_csv("car data.csv")

# First 5 Rows
print("First 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Info:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())





import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("car data.csv")

# Histogram of Selling Price
plt.hist(df['Selling_Price'])

plt.title("Selling Price Distribution")
plt.xlabel("Selling Price")
plt.ylabel("Frequency")

plt.show()


#Graph 2: Present Price vs Selling Price
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("car data.csv")

# Scatter Plot
plt.scatter(df['Present_Price'], df['Selling_Price'])

plt.title("Present Price vs Selling Price")
plt.xlabel("Present Price")
plt.ylabel("Selling Price")

plt.show()



Final Model: Random Forest Regressor
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load Dataset
df = pd.read_csv("car data.csv")

# Feature Engineering
df['Car_Age'] = 2025 - df['Year']

# Remove unnecessary columns
df.drop(['Car_Name', 'Year'], axis=1, inplace=True)

# Convert categorical data into numerical data
df = pd.get_dummies(df, drop_first=True)

# Features and Target
X = df.drop('Selling_Price', axis=1)
y = df['Selling_Price']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Predictions
pred = model.predict(X_test)

# Evaluation
print("MAE:", mean_absolute_error(y_test, pred))
print("R2 Score:", r2_score(y_test, pred))
