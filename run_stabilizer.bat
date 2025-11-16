@echo off
REM ============================
REM SM System Stabilizer Launcher
REM ============================

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to PATH.
    echo Please install Python 3.x and add it to your system PATH.
    pause
    exit /b
)

REM Run the CLI script
python sm_stabilizer.py

pause
