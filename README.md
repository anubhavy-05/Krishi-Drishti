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
- to run this code we have to  use vs code `main.py`script from terminal:
 ```bash
 python main.py
 ```

#  File Structure
- crop_price_prediction.py - Main application file
 
- all_crop_data.csv - Generated data file (created during execution)

- *.joblib files - Trained model files (created during execution)

# Model Details
- Algorithm: Random Forest Regressor

- Features: Rainfall, Demand, Month, Day of week, 7-day moving average

- Training Data: 1000 days of synthetic data per crop-state combination

### Notes
<details><summary>Details about my project in simple language</summary>
# 🌾 Agricultural Commodities Price Prediction using Machine Learning  

## 📌 Introduction  
Agriculture sector humare economy ka backbone hai, lekin sabse badi problem hai **commodity price volatility** (daam ka utar-chadhav). Farmers ki income, food supply chain ka stability aur national planning sab isi pe depend karta hai.  

Traditional methods (historical averages ya manual analysis) slow hote hain aur complex patterns samajhne mein weak hote hain.  

👉 Is project ka main focus hai ek **Machine Learning based system** banana jo **agricultural commodities ke daam ko predict** kare. Historical data (prices, weather, market arrivals, macroeconomic indicators) ko use karke, ML models **accurate aur timely forecasting** denge.  

Yeh system farmers, traders aur policymakers ko:  
- Better decision making 🧑‍🌾  
- Risk kam karne 🔐  
- Profit aur stability improve karne 📈  
mein help karega.  

---

## 🎯 Objectives  

Main objective: Ek **ML model design aur deploy** karna jo **commodities ke daam accurately predict** kare.  

### Sub-objectives:  
- 📊 **Data Aggregation**: Prices, weather, production, aur economic data collect aur merge karna.  
- ⚙️ **Feature Engineering**: Price pe impact karne wale important features banana.  
- 🤖 **Model Development**: Multiple ML models train/test karke best select karna.  
- 🔗 **System Implementation**: Data se prediction tak complete pipeline (API ke saath).  
- 💡 **Actionable Insights**: Farmers aur traders ko decision support dena.  

---

## 📍 Scope  

### ✅ In-Scope:  
- **Commodities**: Wheat, Rice, Pulses (Tur), Onion.  
- **Region**: Indian mandis (Agmarknet data).  
- **Prediction Horizon**: 7 – 30 din ka forecast.  
- **Users**: Farmers, traders, cooperatives, govt. departments.  

### ❌ Out-of-Scope:  
- Automated trading system.  
- Global exchange price predictions.  
- Black swan events (pandemic, war, etc.).  

---

## 🛠️ Features (Feature Engineering)  

Model ki accuracy depend karegi **input features** pe.  

| Category            | Feature Name            | Description |
|----------------------|--------------------------|-------------|
| **Time-Series Data** | Lag Prices (P_t−1, P_t−7) | Pichle din/hafton ke daam |
|                      | Moving Averages (MA_7, MA_30) | Price trends ko capture karna |
|                      | Volatility | Price ka stability measure |
| **Market Data**      | Market Arrivals (Supply) | Mandi mein commodity ka aana |
|                      | Trading Volume | Din ka total trading quantity |
|                      | MSP | Govt. support price |
| **Weather Data**     | Temperature, Rainfall, Humidity, Extreme Events | Crop growth aur health indicators |
| **Agriculture Data** | Sowing Area, Production Estimates, NDVI | Yield aur crop health |
| **Temporal Data**    | Day, Month, Season | Seasonal & harvesting patterns |
| **Economic Data**    | Fuel Prices, Inflation (CPI), Global Prices | Macro factors & transport costs |

---

## 🏗️ System Architecture  

1. **Data Collection**  
   - Sources: Agmarknet (prices), IMD (weather), Ministry of Agriculture (production, MSP), Public APIs (economic).  
   - Storage: PostgreSQL / Data lake.  

2. **Data Preprocessing**  
   - Cleaning: Missing values & outliers handle karna.  
   - Scaling: MinMaxScaler / StandardScaler.  
   - Feature Engineering: Lag, MA, seasonal flags.  

3. **Model Training & Evaluation**  
   - Data split (time-series based).  
   - Algorithms train + Hyperparameter tuning.  
   - Metrics: MAE, RMSE, R².  

4. **Prediction Engine (API)**  
   - Best model serialize karna.  
   - REST API (Flask/FastAPI).  

5. **Deployment & UI**  
   - Cloud (AWS/GCP).  
   - Web dashboard / Mobile app.  

6. **Monitoring & Retraining**  
   - Quarterly retraining with new data.  

---

## 🤖 Algorithms  

- **Baseline Models**: ARIMA, SARIMA (time-series).  
- **Tree-Based Models**: Random Forest, XGBoost, LightGBM.  
- **Deep Learning Models**:  
  - LSTM (sequence learning).  
  - GRU (lighter, faster).  

---

## 🧩 Final Model (Hybrid Approach)  

- **Problem**: Regression task → Predict future price (P_t+k) using features X_t.  
- **Architecture**:  
  - LSTM → Time-series features.  
  - XGBoost → Static + contextual features.  
  - Final Layer → Linear regression / weighted average for combined output.  

- **Deployment**: REST API microservice.  
- **Output**: Price prediction + confidence interval.  

---

## 🚀 Deployment  

- Cloud hosted (AWS/GCP).  
- REST API for integration.  
- User-friendly **dashboard/mobile app** for farmers & traders.  

---

## ✅ Conclusion  

Yeh project **agriculture commodity price forecasting** ko smarter, faster aur reliable banata hai.  
- Farmers → Best time to sell 🌱  
- Traders → Smart buying decisions 💰  
- Policymakers → Food security planning 🏛️  

👉 Hybrid ML model (LSTM + XGBoost) ensures **better accuracy + robustness**.  

---

👨‍💻 *Developed for empowering agriculture with Machine Learning & Data Science.*  

 
</details>

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

