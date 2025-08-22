import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import os

def create_placeholder_data(file_path):
    """
    Generates a placeholder CSV file with dummy data for a crop.
    This function is for demonstration purposes. In a real-world scenario,
    you would replace this with your actual data loading logic.
    """
    print(f"Generating placeholder data for '{file_path}'...")
    date_range = pd.date_range(start='2020-01-01', periods=1000, freq='D')
    df_placeholder = pd.DataFrame({
        'Date': date_range,
        'Price': np.random.rand(1000) * 100 + 1000,
        'Rainfall': np.random.rand(1000) * 50,
        'Demand': np.random.rand(1000) * 200 + 500
    })
    df_placeholder.to_csv(file_path, index=False)
    print("Placeholder data created.")

def train_and_evaluate_crop_model(crop_name, file_path):
    """
    Trains a price prediction model for a specific crop and evaluates its performance.

    Args:
        crop_name (str): The name of the crop (e.g., 'Paddy', 'Maize').
        file_path (str): The path to the CSV file containing the crop data.
    """
    print(f"\n--- Starting process for {crop_name} ---")

    # --- 1. Data Loading and Preprocessing ---
    print("Step 1: Loading and Preprocessing Data...")
    try:
        df = pd.read_csv(file_path)
        print(f"Data for {crop_name} loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        print("Skipping this crop. Please ensure your data file exists.")
        return

    # Check for essential columns
    required_cols = ['Date', 'Price', 'Rainfall', 'Demand']
    if not all(col in df.columns for col in required_cols):
        print(f"Error: The file for {crop_name} must contain 'Date', 'Price', 'Rainfall', and 'Demand' columns.")
        return

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

    # Use a random split for simplicity
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Training set size: {X_train.shape[0]} samples")
    print(f"Test set size: {X_test.shape[0]} samples")

    # --- 4. Model Training ---
    print("\nStep 4: Training the Machine Learning Model...")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("Model training complete.")

    # --- 5. Model Evaluation ---
    print("\nStep 5: Evaluating the Model...")
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"R-squared (R2) Score: {r2:.2f}")

    # --- 6. Displaying the Results in a Table ---
    print("\nStep 6: Displaying the Results in a Table...")
    # Create a DataFrame for easy viewing of actual vs. predicted values
    results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    results_df.sort_index(inplace=True)
    # Print the DataFrame to the console
    print(results_df)

    print("\nProcess completed.")


# --- Main execution loop for different crops ---
if __name__ == "__main__":
    # Define the crops and their respective (placeholder) file paths
    # In a real scenario, you would replace these with your actual data files.
    crop_data_files = {
        'Wheat': 'wheat_price_data.csv',
        'Paddy': 'paddy_price_data.csv',
        'Maize': 'maize_price_data.csv',
        'Arhar': 'arhar_price_data.csv',
        'Cotton': 'cotton_price_data.csv',
        'Moong': 'moong_price_data.csv',
        'Mustard': 'mustard_price_data.csv',
        'Sugarcane': 'sugarcane_price_data.csv'
    }

    # Generate placeholder data for all crops
    for file in crop_data_files.values():
        create_placeholder_data(file)

    # Loop through each crop and run the model
    for crop, file in crop_data_files.items():
        train_and_evaluate_crop_model(crop, file)
        print("\n" + "="*70 + "\n")

    # Clean up the generated placeholder files
    print("Cleaning up placeholder files...")
    for file in crop_data_files.values():
        if os.path.exists(file):
            os.remove(file)
    print("Cleanup complete. All placeholder files removed.")
