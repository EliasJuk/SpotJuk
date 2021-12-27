cd venv/Scripts/
call activate.bat
cd ../../	

set FLASK_ENV=development
set FLASK_APP=src/app.py
call flask run