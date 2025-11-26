import subprocess
import sys
import os
from pathlib import Path

# Kill any stuck Python processes
os.system("taskkill /IM python.exe /F 2>nul || true")

# Install opencv-python
print("Installing opencv-python...")
subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python", "-q"])

# Change to project directory
project_dir = Path("C:/Users/heman/Downloads/DeepFake-Detection-master/DeepFake-Detection-master")
os.chdir(project_dir)

# Create dummy datasets
print("Creating dummy datasets...")
from create_dummy_datasets import *

# Run main.py
print("\n" + "="*80)
print("Running main.py...")
print("="*80 + "\n")
os.system("python main.py")
