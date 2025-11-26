#!/usr/bin/env python3
"""
Main runner for the DeepFake Detection project.
This script handles all setup and runs main.py.
"""
import subprocess
import sys
import os
from pathlib import Path
import json

output_log = []

def log(msg):
    print(msg)
    output_log.append(msg)

# Kill stuck processes
log("Killing any stuck Python processes...")
os.system("taskkill /IM python.exe /F 2>nul || exit /b 0")

# Install opencv
log("Installing opencv-python...")
result = subprocess.run(
    [sys.executable, "-m", "pip", "install", "opencv-python", "-q"],
    capture_output=True,
    text=True
)
if result.returncode != 0:
    log(f"WARNING: pip install returned {result.returncode}\n{result.stderr}")
else:
    log("opencv-python installed successfully")

# Change to project directory
project_dir = Path("C:/Users/heman/Downloads/DeepFake-Detection-master/DeepFake-Detection-master")
os.chdir(project_dir)
log(f"Changed to: {os.getcwd()}")

# Create datasets
log("Creating dummy datasets...")
try:
    from create_dummy_datasets import *
    log("Dummy datasets created successfully")
except Exception as e:
    log(f"ERROR creating datasets: {e}")
    import traceback
    log(traceback.format_exc())

# Run main.py
log("\n" + "="*80)
log("Running main.py...")
log("="*80 + "\n")

result = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)
log(result.stdout)
if result.stderr:
    log("STDERR:\n" + result.stderr)

# Write summary
log("\n" + "="*80)
log(f"Exit code: {result.returncode}")
log("="*80)

# Save log
with open("run_output.log", "w") as f:
    f.write("\n".join(output_log))

log(f"\nFull log saved to: run_output.log")
