#!/usr/bin/env python3
"""
Quick Start Script for Driver Profitability Dashboard

This script helps you quickly set up and run the dashboard.
"""

import subprocess
import sys
import os
import platform

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing packages: {e}")
        return False

def run_dashboard():
    """Run the Streamlit dashboard"""
    print("🚀 Starting Driver Profitability Dashboard...")
    print("📊 The dashboard will open in your browser automatically")
    print("🔄 If it doesn't open, navigate to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the dashboard")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\n👋 Dashboard stopped by user")
    except Exception as e:
        print(f"❌ Error running dashboard: {e}")

def main():
    """Main function"""
    print("🚗 Driver Profitability Dashboard - Quick Start")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Check if requirements.txt exists
    if not os.path.exists("requirements.txt"):
        print("❌ Error: requirements.txt not found")
        print("Make sure you're in the correct directory")
        sys.exit(1)
    
    # Check if app.py exists
    if not os.path.exists("app.py"):
        print("❌ Error: app.py not found")
        print("Make sure you're in the correct directory")
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Run dashboard
    run_dashboard()

if __name__ == "__main__":
    main() 