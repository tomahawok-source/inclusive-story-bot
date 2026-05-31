#!/bin/bash

# Setup Script per Inclusive Story Bot
# Questo script configura tutto automaticamente

set -e  # Esci se ci sono errori

echo "╔════════════════════════════════════════════╗"
echo "║  🚀 SETUP INCLUSIVE STORY BOT 🚀          ║"
echo "╚════════════════════════════════════════════╝"
echo ""

# Controlla Python
echo "📍 Checking Python..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 non trovato. Installa Python 3.9+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo "✅ Python $PYTHON_VERSION trovato"
echo ""

# Crea virtual environment
echo "🔧 Creando virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✅ Virtual environment creato"
else
    echo "✅ Virtual environment già esiste"
fi
echo ""

# Attiva venv
echo "🔌 Attivando virtual environment..."
source venv/bin/activate
echo "✅ Virtual environment attivato"
echo ""

# Upgrade pip
echo "📦 Aggiornando pip..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
echo "✅ pip aggiornato"
echo ""

# Installa dipendenze
echo "📚 Installando dipendenze (questo potrebbe richiedere 5-10 minuti)..."
pip install -r backend/requirements.txt
echo "✅ Dipendenze installate"
echo ""

# Crea .env se non esiste
if [ ! -f ".env" ]; then
    echo "📝 Creando .env..."
    cp .env.example .env
    echo "✅ .env creato"
    echo "   (Puoi modificarlo se necessario)"
else
    echo "✅ .env già esiste"
fi
echo ""

# Crea cartelle necessarie
echo "📁 Creando cartelle..."
mkdir -p logs
mkdir -p generated_images
mkdir -p tests
echo "✅ Cartelle create"
echo ""

echo "╔════════════════════════════════════════════╗"
echo "║  ✅ SETUP COMPLETATO! ✅                  ║"
echo "╚════════════════════════════════════════════╝"
echo ""
echo "🎯 PROSSIMI PASSI:"
echo ""
echo "1️⃣  Attiva l'ambiente:"
echo "   source venv/bin/activate"
echo ""
echo "2️⃣  Avvia il backend:"
echo "   python backend/main.py"
echo ""
echo "3️⃣  In un altro terminale, testa:"
echo "   bash test.sh"
echo ""
echo "✨ Oppure, per tutto in uno:"
echo "   make run"
echo ""
