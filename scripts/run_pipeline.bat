@echo off
echo Starting FDA BI Pipeline...
cd /d C:\Users\ramke\OneDrive\Desktop\fda_pipeline
call venv\Scripts\activate
python pipeline.py
echo Pipeline completed!
pause