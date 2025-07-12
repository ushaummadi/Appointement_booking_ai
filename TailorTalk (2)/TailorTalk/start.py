#!/usr/bin/env python3
"""
Start script for TailorTalk deployment
Runs both backend and frontend services
"""
import subprocess
import threading
import time
import sys
import os

def run_backend():
    """Run the FastAPI backend"""
    print("Starting FastAPI backend...")
    os.chdir("backend")
    subprocess.run([sys.executable, "main.py"])

def run_frontend():
    """Run the Streamlit frontend"""
    print("Starting Streamlit frontend...")
    time.sleep(2)  # Give backend a moment to start
    subprocess.run([
        "streamlit", "run", "app.py", 
        "--server.port=5000", 
        "--server.address=0.0.0.0",
        "--server.headless=true"
    ])

if __name__ == "__main__":
    print("🚀 Starting TailorTalk Calendar Assistant...")
    
    # Start backend in a separate thread
    backend_thread = threading.Thread(target=run_backend, daemon=True)
    backend_thread.start()
    
    # Start frontend in main thread
    try:
        run_frontend()
    except KeyboardInterrupt:
        print("\n✅ TailorTalk stopped")
        sys.exit(0)