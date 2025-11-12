# Krishi Drishti - Quick Start Script
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Starting Krishi Drishti Server" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if virtual environment exists
if (Test-Path "venv") {
    Write-Host "✓ Activating virtual environment..." -ForegroundColor Green
    .\venv\Scripts\Activate.ps1
} else {
    Write-Host "! No virtual environment found, using global Python" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Starting Flask server..." -ForegroundColor Cyan
Write-Host "⚠️  First startup will take 2-5 minutes to train ML models" -ForegroundColor Yellow
Write-Host ""
Write-Host "Once running, open your browser to:" -ForegroundColor Green
Write-Host "  http://localhost:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop the server" -ForegroundColor Yellow
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

python app.py
