@echo off
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate
python.exe -m pip install -r requirements.txt
echo All packages installed.
pause
