# Crop Price Prediction System
A machine learning-based application that predicts crop prices for various crops across different Indian states.

# Overview
This Python application uses a Random Forest regression model to predict crop prices based on historical data, rainfall, and market demand. The system supports multiple crops across different states and provides an interactive command-line interface for predictions.

# Features
- Predicts prices for 8 different crops across various Indian states

- State-specific models for accurate regional predictions

- Interactive command-line interface

- Automated data generation for demonstration

- Model persistence and management

# Supported Crops and States

This document lists the crops and the corresponding Indian states that support them.

| Crop      | Supported States                            |
|-----------|---------------------------------------------|
| Wheat     | Uttar Pradesh, Punjab, Madhya Pradesh       |
| Paddy     | West Bengal, Punjab, Uttar Pradesh          |
| Sugarcane | Uttar Pradesh, Maharashtra                  |
| Maize     | Madhya Pradesh, Uttar Pradesh               |
| Arhar     | Maharashtra, Madhya Pradesh, Uttar Pradesh  |
| Moong     | Rajasthan, Madhya Pradesh                   |
# Installation
1. Ensure you have Python 3.7+ installed

2. Install the required dependencies:

bash

pip install pandas numpy scikit-learn joblib

# Usage
1.Run the application:

bash
python crop_price_prediction.py
2.Follow the interactive prompts:

Select a crop from the available options

Choose a state where that crop is supported

Enter a prediction date in YYYY-MM-DD format

Provide rainfall (in mm) and demand values

3.The system will display the predicted price in ₹ per quintal

4.Type 'quit' to exit the program

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


