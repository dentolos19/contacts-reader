@echo off
cd /d %~dp0
if not exist .venv (
    py -m venv .venv
)
call .venv/Scripts/activate.bat
REM pip install -r requirements.txt >nul