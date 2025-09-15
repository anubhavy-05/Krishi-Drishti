# Crop Price Prediction System
A machine learning-based application that predicts crop prices for various crops across different Indian states.

# Overview
This Python application uses a Random Forest regression model to predict crop prices based on historical data, rainfall, and market demand. The system supports multiple crops across different states and provides an interactive command-line interface for predictions.

# Features
- 🎯 Multi-crop Support: Predicts prices for 8 different crops

- 🗺️ State-specific Models: Trains separate models for each crop-state combination

- 📊 Interactive Interface: User-friendly command-line interface for predictions

- 🔄 Data Generation: Automatically creates placeholder data for demonstration

- 💾 Model Persistence: Saves trained models for future use

- 📈 Time-series Features: Incorporates temporal patterns in pricing data

- 🧹 Auto-cleanup: Removes generated files after session completion

# Crop Price Prediction System Overview

This document provides an overview of supported crops, their corresponding states, and their base prices.

| Crop      | Supported States                            | Base Price (₹/quintal) |
|-----------|---------------------------------------------|------------------------|
| Wheat     | Uttar Pradesh, Punjab, Madhya Pradesh       | 2,125                  |
| Paddy     | West Bengal, Punjab, Uttar Pradesh          | 2,040                  |
| Sugarcane | Uttar Pradesh, Maharashtra                  | 350                    |
| Maize     | Madhya Pradesh, Uttar Pradesh               | 1,962                  |
| Arhar     | Maharashtra, Madhya Pradesh, Uttar Pradesh  | 6,300                  |
| Moong     | Rajasthan, Madhya Pradesh                   | 6,800                  |
| Cotton    | Gujarat, Maharashtra, Punjab                | 7,500                  |
| Mustard   | Rajasthan, Madhya Pradesh                   | 5,500                  |
# Installation
1. **Ensure you have Python 3.7+ installed**

2. **Install the required dependencies:**

``` bash

pip install pandas numpy scikit-learn joblib
```

# Usage
1.**Run the application:**

```bash
python crop_price_prediction.py
```
2.**Follow the interactive prompts:**

 Select a crop from the available options

Choose a state where that crop is supported

Enter a prediction date in YYYY-MM-DD format

Provide rainfall (in mm) and demand values

3.**The system will display the predicted price in ₹ per quintal**

4.**Type 'quit' to exit the program**

# How It Works
## Data Generation
- The system generates synthetic data for demonstration purposes, including:

- Historical price data with realistic trends

- Rainfall and demand metrics

- State-specific price variations

# Model Training
- Uses Random Forest Regressor with 100 estimators

- Creates time-based features (month, day of week, moving averages)

- Trains separate models for each crop-state combination

- Saves models as .joblib files for future use

# Prediction
- Loads the appropriate model based on crop and state

- Processes input features (date, rainfall, demand)

- Returns a price prediction based on the trained model
- ## Run and Script ##
- to run this code we have to  use vs code
- `` main.py``

#  File Structure
- crop_price_prediction.py - Main application file
 
- all_crop_data.csv - Generated data file (created during execution)

- *.joblib files - Trained model files (created during execution)

# Model Details
- Algorithm: Random Forest Regressor

- Features: Rainfall, Demand, Month, Day of week, 7-day moving average

- Training Data: 1000 days of synthetic data per crop-state combination

# Notes
- This implementation uses synthetic data for demonstration purposes

- For production use, replace with actual historical agricultural data

- All generated files are automatically cleaned up when the program exits

# Future Enhancements
- Integration with real agricultural data APIs

- Additional features like temperature, soil conditions

- Web interface or API endpoints

- Historical price visualization

- Model performance evaluation metrics

# License
This project is for educational/demonstration purposes.
# Disclaimer
This software uses synthetic data and is for demonstration purposes only. Predictions should not be used for actual agricultural decision-making without validation against real data and expert consultation.

For questions or suggestions regarding this implementation, please ensure you have reviewed the documentation above thoroughly.

