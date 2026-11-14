@echo off
cd /d C:\Users\Derev\Desktop\project
echo %date% %time% start >> logs\pipeline.log
.venv\Scripts\python.exe src\pipeline.py >> logs\pipeline.log 2>&1