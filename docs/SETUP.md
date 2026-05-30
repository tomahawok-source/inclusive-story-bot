# Setup Guide per Inclusive Story Bot

## 🚀 Quick Start (5 minuti)

### Opzione 1: Setup Locale Semplice

#### 1. Requisiti
```bash
- Python 3.9+
- pip
- Git
```

#### 2. Clona il repository
```bash
git clone https://github.com/tomahawok-source/inclusive-story-bot.git
cd inclusive-story-bot
```

#### 3. Crea virtual environment
```bash
python -m venv venv

# Attiva l'ambiente
source venv/bin/activate  # Su Windows: venv\Scripts\activate
```

#### 4. Installa dipendenze
```bash
pip install -r backend/requirements.txt
```

#### 5. Configura .env
```bash
cp .env.example .env

# Modifica .env con i tuoi valori
# - DISCORD_TOKEN (se usi Discord)
# - TELEGRAM_TOKEN (se usi Telegram)
```

#### 6. Avvia il backend
```bash
cd backend
python main.py
```

L'API sarà disponibile su `http://localhost:8000`

---

## 🤖 Setup Bot

### Discord Bot

#### 1. Crea il bot su Discord Developer Portal
- Vai a https://discord.com/developers/applications
- Clicca "New Application"
- Vai su "Bot" → "Add Bot"
- Copia il token e mettilo in `.env` come `DISCORD_TOKEN`

#### 2. Dai permessi al bot
- Vai su "OAuth2" → "URL Generator"
- Seleziona scopes: `bot`, `applications.commands`
- Seleziona permissions: `Send Messages`, `Read Messages`, `Attach Files`, `Embed Links`
- Copia l'URL e aggiungilo ai tuoi server

#### 3. Avvia il bot
```bash
python bots/discord_bot.py
```

#### 4. Usa i comandi
```
/genimage obese dark "insegnante che spiega"
/corporature
/colori
```

---

### Telegram Bot

#### 1. Crea il bot con BotFather
- Apri Telegram e cerca `@BotFather`
- Scrivi `/newbot`
- Segui le istruzioni
- Copia il token e mettilo in `.env` come `TELEGRAM_TOKEN`

#### 2. Avvia il bot
```bash
python bots/telegram_bot.py
```

#### 3. Usa i comandi
```
/start
/genimage
/corporature
/colori
```

---

## 🐳 Setup con Docker

### Prerequisiti
- Docker
- Docker Compose
- NVIDIA GPU (opzionale ma consigliato)

### 1. Configura .env
```bash
cp .env.example .env

# Aggiungi i tuoi token
DISCORD_TOKEN=your_token_here
TELEGRAM_TOKEN=your_token_here
```

### 2. Build e avvia i container
```bash
docker-compose up --build
```

### 3. Verifica che tutto funzioni
```bash
# Test dell'API
curl http://localhost:8000/health

# Dovresti ricevere:
# {"status":"healthy","version":"1.0.0","model_loaded":true,"gpu_available":true}
```

---

## ☁️ Deployment su Cloud

### Railway
1. Connetti il tuo GitHub
2. Importa il repo
3. Aggiungi le variabili d'ambiente
4. Deploy automatico

### Hugging Face Spaces
1. Crea uno Space
2. Connetti il repository
3. Imposta le variabili d'ambiente
4. Deploy

---

## 🔍 Troubleshooting

### Errore: "ModuleNotFoundError: No module named 'torch'"
```bash
# Reinstalla le dipendenze
pip install --upgrade torch transformers
```

### Errore: "CUDA out of memory"
```bash
# Usa CPU instead di GPU
# Nel .env: USE_GPU=false
```

### Errore: "API connection refused"
```bash
# Assicurati che il backend sia avviato
python backend/main.py

# Verifica che l'API_URL sia corretta nel .env
```

### Errore: "Discord token invalid"
```bash
# Verifica che il token sia corretto
# Non pubblicare mai il token su GitHub!
```

---

## 📚 Prossimi Passi

1. ✅ Configura il backend
2. ✅ Configura almeno un bot (Discord/Telegram)
3. ✅ Testa la generazione di immagini
4. ⭐ Invita il bot nei tuoi server
5. 🚀 Condividi con la comunità!

---

## 📞 Supporto

- 📧 Apri un'issue su GitHub
- 💬 Discussioni su GitHub
- 🐛 Report bug dettagliati

---

**Fatto con ❤️ per una rappresentazione inclusiva**
