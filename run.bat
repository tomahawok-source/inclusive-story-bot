@echo off
REM Run Script per Inclusive Story Bot - Windows
REM Questo script avvia il backend

setlocal enabledelayedexpansion

cls
echo ╔════════════════════════════════════════════╗
echo ║  🚀 AVVIO INCLUSIVE STORY BOT 🚀          ║
echo ╚════════════════════════════════════════════╝
echo.

REM Verifica venv
if not exist "venv" (
    echo ❌ Virtual environment non trovato!
    echo.
    echo Esegui prima:
    echo   setup.bat
    pause
    exit /b 1
)

REM Attiva venv
call venv\Scripts\activate.bat

echo 📁 Backend directory: .\backend
echo 🔧 Attivando virtual environment...
echo 🚀 Avviando server...
echo.
echo 💡 API disponibile su: http://localhost:8000
echo 📚 Documentazione: http://localhost:8000/docs
echo.
echo Per testare, in un altro terminale esegui:
echo   python test.py
echo.
echo ─────────────────────────────────────────────
echo.

python backend\main.py
