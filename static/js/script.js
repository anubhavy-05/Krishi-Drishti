// ===========================
// Global Variables
// ===========================
let cropsData = {};
let keepAliveInterval = null;

// ===========================
// Initialize App
// ===========================
document.addEventListener('DOMContentLoaded', function() {
    loadCropsData();
    setupEventListeners();
    startKeepAlive();
    setTodayDate();
    initScrollProgress();
    addScrollAnimations();
});

// ===========================
// Scroll Progress Bar
// ===========================
function initScrollProgress() {
    const progressBar = document.getElementById('scrollProgress');
    
    window.addEventListener('scroll', () => {
        const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        progressBar.style.width = scrolled + '%';
    });
}

// ===========================
// Scroll Animations
// ===========================
function addScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all cards and sections
    document.querySelectorAll('.card, .feature-card, .intro-section').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// ===========================
// Load Crops Data from API
// ===========================
async function loadCropsData() {
    try {
        showConnectionStatus('connected');
        const response = await fetch('/api/crops');
        const result = await response.json();
        
        if (result.success) {
            cropsData = result.data;
            populateCropDropdown();
        } else {
            showError('Failed to load crops data');
        }
    } catch (error) {
        console.error('Error loading crops:', error);
        showError('Failed to connect to server. Please check your connection.');
        showConnectionStatus('disconnected');
    }
}

// ===========================
// Populate Crop Dropdown
// ===========================
function populateCropDropdown() {
    const cropSelect = document.getElementById('crop');
    cropSelect.innerHTML = '<option value="">-- Choose a crop --</option>';
    
    const sortedCrops = Object.keys(cropsData).sort();
    sortedCrops.forEach(crop => {
        const option = document.createElement('option');
        option.value = crop;
        option.textContent = crop;
        cropSelect.appendChild(option);
    });
}

// ===========================
// Populate State Dropdown
// ===========================
function populateStateDropdown(crop) {
    const stateSelect = document.getElementById('state');
    
    if (!crop || !cropsData[crop]) {
        stateSelect.innerHTML = '<option value="">-- First select a crop --</option>';
        stateSelect.disabled = true;
        return;
    }
    
    stateSelect.innerHTML = '<option value="">-- Choose a state --</option>';
    const states = cropsData[crop];
    
    states.forEach(state => {
        const option = document.createElement('option');
        option.value = state;
        option.textContent = state;
        stateSelect.appendChild(option);
    });
    
    stateSelect.disabled = false;
}

// ===========================
// Setup Event Listeners
// ===========================
function setupEventListeners() {
    // Crop selection change
    document.getElementById('crop').addEventListener('change', function() {
        populateStateDropdown(this.value);
    });
    
    // Form submission
    document.getElementById('predictionForm').addEventListener('submit', handleFormSubmit);
    
    // Form reset
    document.getElementById('predictionForm').addEventListener('reset', function() {
        hideResults();
        hideError();
        const stateSelect = document.getElementById('state');
        stateSelect.innerHTML = '<option value="">-- First select a crop --</option>';
        stateSelect.disabled = true;
    });
}

// ===========================
// Handle Form Submission
// ===========================
async function handleFormSubmit(e) {
    e.preventDefault();
    
    hideError();
    hideResults();
    
    const formData = {
        crop: document.getElementById('crop').value,
        state: document.getElementById('state').value,
        date: document.getElementById('date').value,
        rainfall: parseFloat(document.getElementById('rainfall').value),
        demand: parseFloat(document.getElementById('demand').value)
    };
    
    // Show loading state
    const predictBtn = document.getElementById('predictBtn');
    const btnText = predictBtn.querySelector('.btn-text');
    const btnLoader = predictBtn.querySelector('.btn-loader');
    
    btnText.style.display = 'none';
    btnLoader.style.display = 'flex';
    predictBtn.disabled = true;
    
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        
        if (result.success) {
            displayResults(result.data);
        } else {
            showError(result.error || 'Failed to make prediction');
        }
    } catch (error) {
        console.error('Error making prediction:', error);
        showError('Failed to connect to server. Please try again.');
        showConnectionStatus('disconnected');
    } finally {
        // Hide loading state
        btnText.style.display = 'inline';
        btnLoader.style.display = 'none';
        predictBtn.disabled = false;
    }
}

// ===========================
// Display Results
// ===========================
function displayResults(data) {
    document.getElementById('predictedPrice').textContent = data.predicted_price.toLocaleString('en-IN', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });
    document.getElementById('resultCrop').textContent = data.crop;
    document.getElementById('resultState').textContent = data.state;
    document.getElementById('resultDate').textContent = formatDate(data.date);
    document.getElementById('resultRainfall').textContent = data.rainfall;
    document.getElementById('resultDemand').textContent = data.demand;
    
    const resultsSection = document.getElementById('resultsSection');
    resultsSection.style.display = 'block';
    
    // Scroll to results
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// ===========================
// Show/Hide Results
// ===========================
function hideResults() {
    document.getElementById('resultsSection').style.display = 'none';
}

// ===========================
// Show/Hide Error
// ===========================
function showError(message) {
    document.getElementById('errorMessage').textContent = message;
    document.getElementById('errorSection').style.display = 'block';
    
    // Scroll to error
    document.getElementById('errorSection').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function hideError() {
    document.getElementById('errorSection').style.display = 'none';
}

function closeError() {
    hideError();
}

// ===========================
// Keep-Alive Mechanism
// ===========================
function startKeepAlive() {
    // Ping server every 10 minutes (600000 ms)
    keepAliveInterval = setInterval(async () => {
        try {
            const response = await fetch('/api/health');
            const result = await response.json();
            
            if (result.success) {
                showConnectionStatus('connected');
                console.log('Keep-alive ping successful:', result.timestamp);
            } else {
                showConnectionStatus('disconnected');
            }
        } catch (error) {
            console.error('Keep-alive ping failed:', error);
            showConnectionStatus('disconnected');
        }
    }, 600000); // 10 minutes
    
    // Also ping immediately when page becomes visible
    document.addEventListener('visibilitychange', async () => {
        if (!document.hidden) {
            try {
                const response = await fetch('/api/health');
                const result = await response.json();
                if (result.success) {
                    showConnectionStatus('connected');
                }
            } catch (error) {
                showConnectionStatus('disconnected');
            }
        }
    });
}

// ===========================
// Connection Status Display
// ===========================
function showConnectionStatus(status) {
    const statusElement = document.getElementById('connectionStatus');
    const statusText = statusElement.querySelector('.status-text');
    
    if (status === 'connected') {
        statusElement.classList.remove('disconnected');
        statusText.textContent = 'Connected';
    } else {
        statusElement.classList.add('disconnected');
        statusText.textContent = 'Disconnected';
    }
}

// ===========================
// Utility Functions
// ===========================
function setTodayDate() {
    const today = new Date().toISOString().split('T')[0];
    document.getElementById('date').value = today;
}

function formatDate(dateString) {
    const date = new Date(dateString);
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-IN', options);
}

// ===========================
// Cleanup on page unload
// ===========================
window.addEventListener('beforeunload', () => {
    if (keepAliveInterval) {
        clearInterval(keepAliveInterval);
    }
});
