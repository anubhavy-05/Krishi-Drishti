from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib
import os
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

# Configuration
SUPPORTED_CROPS_AND_STATES = {
    'Wheat': ['Uttar Pradesh', 'Punjab', 'Madhya Pradesh'],
    'Paddy': ['West Bengal', 'Punjab', 'Uttar Pradesh'],
    'Sugarcane': ['Uttar Pradesh', 'Maharashtra'],
    'Maize': ['Madhya Pradesh', 'Uttar Pradesh'],
    'Arhar': ['Maharashtra', 'Madhya Pradesh', 'Uttar Pradesh'],
    'Moong': ['Rajasthan', 'Madhya Pradesh'],
    'Cotton': ['Gujarat', 'Maharashtra', 'Punjab'],
    'Mustard': ['Rajasthan', 'Madhya Pradesh']
}

DATA_FILE = "all_crop_data.csv"

def train_and_save_crop_model(full_df, crop_name, state_name):
    """Trains a model on a filtered slice of the main DataFrame."""
    print(f"Training Model for {crop_name} in {state_name}...")
    
    df = full_df[(full_df['Crop'] == crop_name) & (full_df['State'] == state_name)].copy()
    
    if df.empty:
        print(f"Warning: No data found for {crop_name} in {state_name}. Skipping.")
        return False
        
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    
    df['month'] = df.index.month
    df['day_of_week'] = df.index.dayofweek
    df['moving_average_7_day'] = df['Price'].rolling(window=7).mean()
    df.dropna(inplace=True)
    
    features = ['Rainfall', 'Demand', 'month', 'day_of_week', 'moving_average_7_day']
    X = df[features]
    y = df['Price']
    
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    model_filename = f"{crop_name.lower()}_{state_name.lower().replace(' ', '_')}_price_model.joblib"
    joblib.dump(model, model_filename)
    print(f"Model saved as '{model_filename}'")
    return True

def initialize_models():
    """Check if data file exists. Models will be trained on-demand."""
    print("="*70)
    print("KRISHI DRISHTI - STARTING UP")
    print("="*70)
    
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found!")
        return False
    
    print(f"✓ Data file found: {DATA_FILE}")
    print("✓ Models will be trained on first prediction request")
    print("="*70)
    return True

def get_or_train_model(crop_name, state_name):
    """Load existing model or train a new one if it doesn't exist."""
    model_file = f"{crop_name.lower()}_{state_name.lower().replace(' ', '_')}_price_model.joblib"
    
    if os.path.exists(model_file):
        print(f"Loading existing model for {crop_name} in {state_name}")
        return joblib.load(model_file)
    
    print(f"Training new model for {crop_name} in {state_name}...")
    full_dataset = pd.read_csv(DATA_FILE)
    success = train_and_save_crop_model(full_dataset, crop_name, state_name)
    
    if success:
        return joblib.load(model_file)
    return None

def predict_crop_price(crop_name, state_name, prediction_date, rainfall, demand):
    """Predicts the price using the trained model."""
    
    # Load or train model on-demand
    model = get_or_train_model(crop_name, state_name)
    if model is None:
        return None, f"Could not load/train model for {crop_name} in {state_name}"
    
    try:
        df_hist_full = pd.read_csv(DATA_FILE)
        df_hist_full['Date'] = pd.to_datetime(df_hist_full['Date'])
        
        df_hist = df_hist_full[(df_hist_full['Crop'] == crop_name) & (df_hist_full['State'] == state_name)]
        if df_hist.empty:
            return None, f"No historical data found for {crop_name} in {state_name}"
    except FileNotFoundError:
        return None, f"Historical data file '{DATA_FILE}' not found."
    
    try:
        pred_date = pd.to_datetime(prediction_date)
        month = pred_date.month
        day_of_week = pred_date.dayofweek
        
        start_date = pred_date - timedelta(days=7)
        end_date = pred_date - timedelta(days=1)
        
        recent_data = df_hist[(df_hist['Date'] >= start_date) & (df_hist['Date'] <= end_date)]
        
        if recent_data.empty:
            moving_avg = df_hist['Price'].iloc[-1]
        else:
            moving_avg = recent_data['Price'].mean()
    except Exception as e:
        return None, f"Error during feature engineering: {str(e)}"
    
    features = ['Rainfall', 'Demand', 'month', 'day_of_week', 'moving_average_7_day']
    input_data = pd.DataFrame([[rainfall, demand, month, day_of_week, moving_avg]], columns=features)
    
    predicted_price = model.predict(input_data)[0]
    return predicted_price, None

# Routes
@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')

@app.route('/api/crops', methods=['GET'])
def get_crops():
    """Return the list of supported crops and states."""
    return jsonify({
        'success': True,
        'data': SUPPORTED_CROPS_AND_STATES
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    """Handle price prediction requests."""
    try:
        data = request.get_json()
        
        # Validate input
        crop = data.get('crop', '').strip().title()
        state = data.get('state', '').strip().title()
        date = data.get('date', '').strip()
        rainfall = float(data.get('rainfall', 0))
        demand = float(data.get('demand', 0))
        
        # Validate crop and state
        if crop not in SUPPORTED_CROPS_AND_STATES:
            return jsonify({
                'success': False,
                'error': f'Unsupported crop: {crop}'
            }), 400
        
        if state not in SUPPORTED_CROPS_AND_STATES[crop]:
            return jsonify({
                'success': False,
                'error': f'State {state} not supported for {crop}'
            }), 400
        
        # Validate date format
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return jsonify({
                'success': False,
                'error': 'Invalid date format. Use YYYY-MM-DD'
            }), 400
        
        # Make prediction
        predicted_price, error = predict_crop_price(crop, state, date, rainfall, demand)
        
        if error:
            return jsonify({
                'success': False,
                'error': error
            }), 500
        
        return jsonify({
            'success': True,
            'data': {
                'crop': crop,
                'state': state,
                'date': date,
                'rainfall': rainfall,
                'demand': demand,
                'predicted_price': round(predicted_price, 2)
            }
        })
    
    except ValueError as e:
        return jsonify({
            'success': False,
            'error': 'Invalid input values. Please check rainfall and demand are numbers.'
        }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An unexpected error occurred: {str(e)}'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint to keep the server alive."""
    return jsonify({
        'success': True,
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    # Initialize models on startup
    initialize_models()
    
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
