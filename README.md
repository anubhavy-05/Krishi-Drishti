# 🌾 Krishi Drishti - Crop Price Prediction System

A machine learning-based web application that predicts crop prices for various crops across different Indian states using advanced Random Forest algorithms.

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

---

## 📋 Overview

Krishi Drishti is a full-stack web application that uses machine learning to predict crop prices based on historical data, rainfall, and market demand. The system supports 8 major crops across multiple Indian states and provides an intuitive web interface for making predictions.

### 🎯 Main Objective
**Design and deploy** a machine learning model that **predicts future market prices of specific agricultural commodities** to help farmers, traders, and policymakers make informed decisions.   

### Sub-objectives:  
- 📊 **Data Aggregation**: Collect and consolidate comprehensive datasets from various sources
- ⚙️ **Feature Engineering**: Identify influential features that drive price fluctuations
- 🤖 **Model Development**: Train and evaluate ML algorithms for accurate price forecasting
- 🔗 **System Implementation**: Create a functional pipeline with a user-friendly web interface
- 💡 **Actionable Insights**: Help farmers, traders, and policymakers make informed decisions

---

## ✨ Features

### 🎯 Core Capabilities
- **Multi-crop Support**: Predicts prices for 8 different crops (Wheat, Paddy, Sugarcane, Maize, Arhar, Moong, Cotton, Mustard)
- **State-specific Models**: Separate trained models for each crop-state combination (24 models total)
- **Web Interface**: Modern, responsive web UI for easy access from any device
- **Real-time Predictions**: Instant price predictions based on user inputs
- **Auto Keep-Alive**: Prevents Render's 15-minute timeout with automatic health checks
- **Data-Driven**: Uses historical prices, weather data, and market demand patterns
- **Time-series Features**: Incorporates temporal patterns including moving averages and seasonal trends

### 🌐 Web Application Features
- � **Beautiful UI**: Modern gradient design with smooth animations
- � **Mobile Responsive**: Works seamlessly on phones, tablets, and desktops
- 🔄 **Dynamic Forms**: Smart dropdowns that update based on crop selection
- � **Visual Results**: Clear display of predictions with detailed breakdown
- ⚡ **Fast Performance**: Optimized for quick predictions and low latency
- 🔌 **Connection Monitor**: Real-time server connection status indicator

---

## 📊 Supported Crops & States

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

---

## 🚀 Deployment Guide

### Option 1: Deploy to Render (Recommended)

1. **Fork this repository** to your GitHub account

2. **Click the Deploy to Render button** at the top of this README

3. **Connect your GitHub repository** to Render

4. Render will automatically:
   - Detect the `render.yaml` configuration
   - Install dependencies from `requirements.txt`
   - Start the application using the `Procfile`
   - Generate ML models on first startup

5. **Access your app** at the provided Render URL (e.g., `https://krishi-drishti.onrender.com`)

**Note**: The free tier on Render spins down after 15 minutes of inactivity. The app includes an automatic keep-alive mechanism that pings the server every 10 minutes when the page is open to prevent this.

### Option 2: Manual Render Deployment

1. Create a new Web Service on [Render](https://render.com)
2. Connect your GitHub repository
3. Configure the service:
   - **Name**: `krishi-drishti`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Deploy!

---

## 💻 Local Development

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/anubhavy-05/Krishi-Drishti.git
   cd Krishi-Drishti
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

### First Run
On the first run, the application will:
- Load the crop data from `all_crop_data.csv`
- Train ML models for all crop-state combinations
- Save trained models as `.joblib` files
- This may take 2-3 minutes

---

## 🏗️ Project Structure

```
Krishi-Drishti/
│
├── app.py                      # Flask backend application
├── main3.py                    # Original CLI-based prediction script
├── more-advance-prediction.py  # Advanced prediction logic
│
├── templates/
│   └── index.html              # Main web interface
│
├── static/
│   ├── css/
│   │   └── styles.css          # Stylesheet with responsive design
│   └── js/
│       └── script.js           # Frontend logic & API calls
│
├── all_crop_data.csv           # Historical crop price data (20,000+ rows)
├── combined_crop_data.csv      # Additional dataset
│
├── requirements.txt            # Python dependencies
├── Procfile                    # Render/Heroku deployment config
├── render.yaml                 # Render infrastructure-as-code
├── .gitignore                  # Git ignore rules
│
└── README.md                   # This file
```

---

## 🔌 API Endpoints

### 1. Get Supported Crops
```http
GET /api/crops
```
**Response:**
```json
{
  "success": true,
  "data": {
    "Wheat": ["Uttar Pradesh", "Punjab", "Madhya Pradesh"],
    "Paddy": ["West Bengal", "Punjab", "Uttar Pradesh"],
    ...
  }
}
```

### 2. Predict Crop Price
```http
POST /api/predict
Content-Type: application/json

{
  "crop": "Wheat",
  "state": "Punjab",
  "date": "2024-12-01",
  "rainfall": 25.5,
  "demand": 650
}
```
**Response:**
```json
{
  "success": true,
  "data": {
    "crop": "Wheat",
    "state": "Punjab",
    "date": "2024-12-01",
    "rainfall": 25.5,
    "demand": 650,
    "predicted_price": 2234.56
  }
}
```

### 3. Health Check (Keep-Alive)
```http
GET /api/health
```
**Response:**
```json
{
  "success": true,
  "status": "healthy",
  "timestamp": "2024-11-13T10:30:00.000000"
}
```

---

## 🤖 How It Works

### Machine Learning Pipeline

1. **Data Loading**: Historical crop price data with weather and demand information
2. **Feature Engineering**:
   - Temporal features: month, day of week
   - Moving averages: 7-day rolling average of prices
   - Input features: rainfall, demand
3. **Model Training**: Random Forest Regressor with 100 estimators
4. **Prediction**: Uses trained models to predict future prices
5. **State Management**: Models are saved and reloaded for fast predictions

### Model Architecture
- **Algorithm**: Random Forest Regressor
- **Features**: 
  - `Rainfall` (mm)
  - `Demand` (market demand value)
  - `month` (1-12)
  - `day_of_week` (0-6)
  - `moving_average_7_day` (7-day price average)
- **Training Data**: 1000 days per crop-state combination
- **Total Models**: 24 models (8 crops × 3 states average)

---

## 🎨 Web Interface Usage

1. **Select Crop**: Choose from 8 available crops
2. **Select State**: Pick a state where the selected crop is grown
3. **Enter Date**: Select the prediction date
4. **Input Rainfall**: Enter expected rainfall in millimeters
5. **Input Demand**: Enter market demand value
6. **Click Predict**: Get instant price prediction in ₹ per quintal

The interface will display:
- Predicted price prominently
- All input parameters for verification
- Connection status (to monitor server availability)

---

## 🔄 Keep-Alive Mechanism

To prevent Render's free tier from spinning down after 15 minutes of inactivity, the application includes:

- **Automatic Health Pings**: JavaScript pings `/api/health` every 10 minutes
- **Visibility Detection**: Re-pings when browser tab becomes active
- **Connection Monitor**: Visual indicator showing server connection status
- **Graceful Handling**: Displays disconnection if server is unavailable

---

## 🛠️ Technologies Used

### Backend
- **Flask**: Python web framework
- **Flask-CORS**: Cross-Origin Resource Sharing
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation
- **numpy**: Numerical computing
- **joblib**: Model serialization
- **gunicorn**: Production WSGI server

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with gradients, animations
- **JavaScript (ES6)**: Async/await, Fetch API
- **Google Fonts**: Poppins font family

### Deployment
- **Render**: Cloud hosting platform
- **Git**: Version control
- **GitHub**: Code repository

---

## 📝 Notes & Disclaimers

- **Synthetic Data**: The current implementation uses generated data for demonstration. For production use, replace with actual historical agricultural data from reliable sources like Agmarknet.
- **Model Accuracy**: Predictions are based on historical patterns and should be used as guidance, not absolute truth.
- **Free Tier Limitation**: Render's free tier may spin down after 15 minutes of inactivity, but the keep-alive mechanism minimizes this issue.
- **First Load**: Initial deployment may take 2-3 minutes as models are trained on startup.

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is for educational/demonstration purposes.

---

## 👨‍💻 Author

**Anubhav** - [@anubhavy-05](https://github.com/anubhavy-05)

---

## 🙏 Acknowledgments

- Historical crop price patterns based on Indian agricultural data
- ML algorithms powered by scikit-learn
- Inspired by the need to empower farmers with data-driven insights

---

## 📧 Contact & Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Review the documentation above thoroughly before raising issues

---

## 🔮 Future Enhancements

- [ ] Integration with real-time agricultural data APIs
- [ ] Additional features like temperature, soil conditions
- [ ] Historical price visualization charts
- [ ] Export predictions to PDF/Excel
- [ ] Multi-language support (Hindi, regional languages)
- [ ] Mobile app version
- [ ] Advanced ML models (LSTM, Prophet)
- [ ] Weather API integration for automatic rainfall data

---

**⭐ If you find this project useful, please consider giving it a star on GitHub!**

---

<details><summary>📖 Detailed Project Documentation (Click to expand)</summary>
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

