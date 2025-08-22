import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# --- 1. Data Loading and Preprocessing ---
print("Step 1: Loading and Preprocessing Data...")

# Load the dataset
try:
    df = pd.read_csv('wheat_price_data.csv')
    print("Data loaded successfully.")
except FileNotFoundError:
    print("Error: The file 'wheat_price_data.csv' was not found.")
    exit()

# Convert the 'Date' column to datetime and set it as the index
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Display the first few rows and data info
print("\nFirst 5 rows of the data:")
print(df.head())
print("\nData Info:")
print(df.info())

# --- 2. Feature Engineering ---
print("\nStep 2: Feature Engineering...")

# Create time-based features
df['month'] = df.index.month
df['day_of_week'] = df.index.dayofweek

# Create a rolling moving average feature
# This is a powerful feature for time-series data
df['moving_average_7_day'] = df['Price'].rolling(window=7).mean()

# Drop rows with NaN values created by the moving average
df.dropna(inplace=True)
print("Features created and rows with NaN values dropped.")

# --- 3. Data Splitting ---
print("\nStep 3: Splitting Data into Training and Testing Sets...")

# Define features (X) and target (y)
features = ['Rainfall', 'Demand', 'month', 'day_of_week', 'moving_average_7_day']
X = df[features]
y = df['Price']

# Use a random split for simplicity, but a time-based split is often better for real projects
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape[0]} samples")
print(f"Test set size: {X_test.shape[0]} samples")

# --- 4. Model Training ---
print("\nStep 4: Training the Machine Learning Model...")

# We'll use RandomForestRegressor, which is robust and effective
model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

print("Model training complete.")

# --- 5. Model Evaluation ---
print("\nStep 5: Evaluating the Model...")

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate performance metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"R-squared (R2) Score: {r2:.2f}")

# --- 6. Visualization ---
print("\nStep 6: Visualizing the Results...")

# Create a DataFrame for easy plotting
results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
results_df.sort_index(inplace=True)

# Plot the results
plt.figure(figsize=(12, 6))
plt.plot(results_df.index, results_df['Actual'], label='Actual Price', color='blue', marker='o')
plt.plot(results_df.index, results_df['Predicted'], label='Predicted Price', color='red', linestyle='--')
plt.title('Wheat Price Prediction: Actual vs. Predicted')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()

print("\nAll steps completed. Check the plot for a visual representation of the model's performance.")
