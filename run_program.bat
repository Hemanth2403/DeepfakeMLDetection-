@echo off
REM Kill Python processes
taskkill /IM python.exe /F 2>nul
timeout /t 1 /nobreak

REM Install OpenCV
python -m pip install opencv-python

REM Create datasets
cd /d "C:\Users\heman\Downloads\DeepFake-Detection-master\DeepFake-Detection-master"
python create_dummy_datasets.py

REM Run the program
python main.py

pause
