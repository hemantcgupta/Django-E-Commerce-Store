@echo off
echo Creating virtual environment...
python -m venv venv
pip install -r requirements.txt
echo All packages installed.
pause
