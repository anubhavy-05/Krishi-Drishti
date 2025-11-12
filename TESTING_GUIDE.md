# Testing Guide for Krishi-Drishti

## Issue Fixed
The dropdown selection issue has been resolved with the following improvements:

### Changes Made:

1. **JavaScript Debugging Added**
   - Added console.log statements throughout the code
   - Better error handling and validation
   - Fixed scroll animation to exclude form elements (was setting opacity to 0)

2. **Event Listener Enhancement**
   - Added validation to ensure form elements exist before attaching listeners
   - Better error reporting in the console

3. **Scroll Animation Fix**
   - Changed from `.card` selector to specific selectors (`.feature-card`, `.intro-section`, `.results-section`)
   - This prevents the prediction form from being hidden by scroll animations

## How to Test Locally:

### Step 1: Install Dependencies (if not done already)
```bash
cd "c:\Users\ay840\Downloads\Krishi\Krishi-Drishti"
pip install -r requirements.txt
```

### Step 2: Start the Flask Server
```bash
python app.py
```

**Note:** The first time you run this, it will take 2-5 minutes to:
- Load the CSV data files
- Train 24 machine learning models (8 crops × 3 states average)
- The console will show progress

### Step 3: Open Browser
Open your web browser and navigate to:
```
http://localhost:5000
```

### Step 4: Test the Dropdowns

1. **Open Browser Console** (Press F12)
   - You'll see debug messages showing:
     - "Loading crops data..."
     - "Crops data received: {data...}"
     - "Crop dropdown populated with X crops"

2. **Select a Crop**
   - Click on the "Select Crop" dropdown
   - Choose any crop (e.g., "Wheat")
   - Console should show: "Crop changed to: Wheat"
   - Console should show: "Populating states for crop: Wheat"
   - Console should show: "State dropdown populated with X states"
   - The State dropdown should now be enabled and populated

3. **Select a State**
   - Choose a state from the now-enabled dropdown

4. **Fill Remaining Fields**
   - Select a date
   - Enter rainfall (mm)
   - Enter demand (tonnes)

5. **Click Predict**
   - Should show loading spinner
   - Should display prediction results

## Debugging Issues:

### If dropdowns don't work:

1. **Check Browser Console** (F12 → Console tab)
   - Look for red error messages
   - Check if "Loading crops data..." appears
   - Check if crops data is received

2. **Check Network Tab** (F12 → Network tab)
   - Look for requests to `/api/crops`
   - Should return status 200 with JSON data

3. **Check Flask Console**
   - Should show "Training model for Crop: X, State: Y"
   - Should show no errors

### Common Issues:

**Issue:** Server starts very slowly
- **Cause:** Training 24 ML models takes time
- **Solution:** Wait 2-5 minutes for initial startup
- **Indicator:** Console shows "Training model for..." messages

**Issue:** `ModuleNotFoundError`
- **Cause:** Missing Python packages
- **Solution:** Run `pip install -r requirements.txt`

**Issue:** Dropdown appears but clicking doesn't populate states
- **Cause:** JavaScript not loaded or API not responding
- **Solution:** Check browser console for errors and verify `/api/crops` returns data

## What to Expect:

### Initial Load:
- Connection indicator should show "Connected"
- Crop dropdown should be populated automatically
- State dropdown should be disabled with "-- First select a crop --"

### After Selecting Crop:
- Console logs the crop selection
- State dropdown becomes enabled
- State dropdown populated with available states for that crop

### After Prediction:
- Loading spinner appears
- Results section slides in with animation
- Shows predicted price with currency formatting

## Production Deployment to Render:

Once local testing is complete:

1. Push code to GitHub repository
2. Click the "Deploy to Render" button in README.md
3. Follow Render's deployment instructions
4. Wait for deployment (first deploy takes 5-10 minutes due to model training)

## Files Modified for Fix:

- `static/js/script.js` - Added extensive debugging and fixed scroll animations
- This testing guide (new file)

The application should now work perfectly with all dropdowns functioning correctly!
