@echo off
REM Setup Script per Inclusive Story Bot - Windows

cls
echo.
echo ╔════════════════════════════════════════════╗
echo ║  🚀 SETUP INCLUSIVE STORY BOT 🚀          ║
echo ╚════════════════════════════════════════════╝
echo.

REM Controlla Python
echo 📍 Checking Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python non trovato. Installa Python 3.9+
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo ✅ Python %PYTHON_VERSION% trovato
echo.

REM Crea virtual environment
echo 🔧 Creando virtual environment...
if not exist "venv" (
    python -m venv venv
    echo ✅ Virtual environment creato
) else (
    echo ✅ Virtual environment già esiste
)
echo.

REM Attiva venv
echo 🔌 Attivando virtual environment...
call venv\Scripts\activate.bat
echo ✅ Virtual environment attivato
echo.

REM Upgrade pip
echo 📦 Aggiornando pip...
python -m pip install --upgrade pip setuptools wheel >nul 2>&1
echo ✅ pip aggiornato
echo.

REM Installa dipendenze
echo 📚 Installando dipendenze (questo potrebbe richiedere 5-10 minuti)...
pip install -r backend\requirements.txt
echo ✅ Dipendenze installate
echo.

REM Crea .env se non esiste
if not exist ".env" (
    echo 📝 Creando .env...
    copy .env.example .env >nul
    echo ✅ .env creato
    echo    ^(Puoi modificarlo se necessario^)
) else (
    echo ✅ .env già esiste
)
echo.

REM Crea cartelle
echo 📁 Creando cartelle...
if not exist "logs" mkdir logs
if not exist "generated_images" mkdir generated_images
if not exist "tests" mkdir tests
echo ✅ Cartelle create
echo.

echo ╔════════════════════════════════════════════╗
echo ║  ✅ SETUP COMPLETATO! ✅                  ║
echo ╚════════════════════════════════════════════╝
echo.
echo 🎯 PROSSIMI PASSI:
echo.
echo 1️⃣  Attiva l'ambiente:
echo    venv\Scripts\activate.bat
echo.
echo 2️⃣  Avvia il backend:
echo    python backend\main.py
echo.
echo 3️⃣  In un altro terminale, testa:
echo    python test.py
echo.
pause
