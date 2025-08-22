import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

def train_and_evaluate_crop_model(crop_name, file_path):
    """
    Trains a price prediction model for a specific crop and evaluates its performance.

    Args:
        crop_name (str): The name of the crop (e.g., 'Paddy', 'Maize').
        file_path (str): The path to the CSV file containing the crop data.
    """
    print(f"--- Processing {crop_name} ---")

    # --- 1. Data Loading and Preprocessing ---
    try:
        df = pd.read_csv(file_path)
        print(f"Data for {crop_name} loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return

    # Check for essential columns
    required_cols = ['Date', 'Price', 'Rainfall', 'Demand']
    if not all(col in df.columns for col in required_cols):
        print(f"Error: The file for {crop_name} must contain 'Date', 'Price', 'Rainfall', and 'Demand' columns.")
        return

    # Convert the 'Date' column to datetime and set it as the index
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)

    # --- 2. Feature Engineering ---
    df['month'] = df.index.month
    df['day_of_week'] = df.index.dayofweek
    df['moving_average_7_day'] = df['Price'].rolling(window=7).mean()
    df.dropna(inplace=True)

    print("Features created and rows with NaN values dropped.")

    # --- 3. Data Splitting ---
    features = ['Rainfall', 'Demand', 'month', 'day_of_week', 'moving_average_7_day']
    X = df[features]
    y = df['Price']

    # Use a random split for simplicity
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- 4. Model Training ---
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model training complete.")

    # --- 5. Model Evaluation ---
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"R-squared (R2) Score: {r2:.2f}")

    # --- 6. Visualization ---
    results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    results_df.sort_index(inplace=True)

    plt.figure(figsize=(12, 6))
    plt.plot(results_df.index, results_df['Actual'], label=f'Actual {crop_name} Price', color='blue', marker='o')
    plt.plot(results_df.index, results_df['Predicted'], label=f'Predicted {crop_name} Price', color='red', linestyle='--')
    plt.title(f'{crop_name} Price Prediction: Actual vs. Predicted')
    plt.xlabel('Date')
    plt.ylabel('Price (INR)')
    plt.legend()
    plt.grid(True)
    plt.show()

# --- Main execution loop for different crops ---
if __name__ == "__main__":
    # Create placeholder CSV files with sample data
    # In a real scenario, you would replace these with your actual data files.
    data_gen_path = 'placeholder_data.csv'
    pd.DataFrame({
        'Date': pd.to_datetime(pd.date_range(start='2020-01-01', periods=100, freq='D')),
        'Price': np.random.rand(100) * 100 + 1000,
        'Rainfall': np.random.rand(100) * 50,
        'Demand': np.random.rand(100) * 200 + 500
    }).to_csv(data_gen_path, index=False)

    # Dictionary mapping crop names to their data file paths
    crop_data_files = {
        'Paddy': data_gen_path,
        'Maize': data_gen_path,
        'Arhar': data_gen_path,
        'Cotton': data_gen_path,
        'Moong': data_gen_path,
        'Mustard': data_gen_path,
        'Sugarcane': data_gen_path
    }

    # Loop through each crop and run the model
    for crop, file in crop_data_files.items():
        train_and_evaluate_crop_model(crop, file)
        print("\n" + "="*50 + "\n")

    # The original wheat model run
    train_and_evaluate_crop_model('Wheat', 'wheat_price_data.csv')