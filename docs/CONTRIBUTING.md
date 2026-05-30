# Contributing Guide

Grazie per l'interesse nel contribuire a Inclusive Story Bot! 🙏

Questo progetto è guidato dalla comunità e dalle persone marginalizzate per il loro corpo e apparenza.

---

## 🎯 Come Contribuire

### 1. Bug Reports
Se trovi un bug:

1. Verifica che non sia già segnalato
2. Crea una **Issue** con:
   - Descrizione chiara del problema
   - Step-by-step per riprodurlo
   - Comportamento atteso vs effettivo
   - Screenshots se possibile
   - Sistema operativo e versione Python

**Titolo Issue:**
```
[BUG] Breve descrizione del problema
```

---

### 2. Feature Requests
Suggerisci nuove features:

1. Descrivi il problema che risolve
2. Proponi una soluzione
3. Dai esempi di utilizzo
4. Considera l'impatto di inclusività

**Titolo Issue:**
```
[FEATURE] Breve descrizione della feature
```

---

### 3. Pull Requests

#### Setup di sviluppo
```bash
# 1. Fork il repository
# 2. Clone il tuo fork
git clone https://github.com/your-username/inclusive-story-bot.git
cd inclusive-story-bot

# 3. Crea un branch
git checkout -b feature/nome-feature

# 4. Crea virtual environment
python -m venv venv
source venv/bin/activate

# 5. Installa dipendenze di dev
pip install -r backend/requirements.txt
pip install pytest pytest-cov black flake8
```

#### Processo di contribuzione

1. **Crea un branch descriptivo:**
   ```bash
   git checkout -b feature/add-more-body-types
   # o
   git checkout -b fix/validation-bug
   ```

2. **Scrivi codice seguendo le linee guida:**
   - Usa nomi variabili chiari
   - Aggiungi docstring
   - Segui PEP 8
   - Massimo 100 caratteri per linea

3. **Scrivi test:**
   ```bash
   pytest tests/
   pytest --cov=backend tests/
   ```

4. **Format del codice:**
   ```bash
   black backend/
   flake8 backend/
   ```

5. **Commit messaggi descrittivi:**
   ```
   feat: add new body type representation
   
   - Aggiunge nuova corporatura "athletic"
   - Include descrizioni inclusive
   - Aggiorna templates di prompt
   ```

6. **Push e apri PR:**
   ```bash
   git push origin feature/add-more-body-types
   ```

#### PR Checklist
Prima di aprire una PR:
- [ ] Codice segue le linee guida
- [ ] Tests aggiunti e passano
- [ ] Documentazione aggiornata
- [ ] No hardcoded values
- [ ] Inclusività verificata

#### Descrizione della PR
```markdown
## Descrizione
Breve descrizione di cosa cambia

## Tipo di Cambio
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation

## Cambios
- Cosa cambia 1
- Cosa cambia 2

## Testing
Come testare i cambiamenti

## Inclusività
Come questo cambio migliora l'inclusività?

## Checklist
- [ ] Tests aggiunti
- [ ] Documentazione aggiornata
- [ ] Nessun warning di linting
```

---

### 4. Miglioramenti della Documentazione

1. Migliora README, guide, o docstrings
2. Aggiungi traduzioni
3. Correggi typo
4. Fornisci esempi migliori

---

### 5. Migliorie di Inclusività

Aree dove aiutare:
- ✨ Migliorare prompt inclusivi
- 🌐 Aggiungere supporto lingue
- 👥 Rappresentare più diversità (disabilità, genere, age)
- 📚 Feedback sulla rappresentazione

---

## 💭 Linee Guida Etiche

### Incluso vs Escluso

**Incluso:**
- Rappresentazione positiva di tutte le corporature
- Dignità universale
- Linguaggio rispettoso
- Diversità nei ruoli

**Escluso:**
- Stereotipi
- Narrativa di "ispirazione porn"
- Pathologizzazione
- Tokenismo

---

## 📝 Aree di Sviluppo Prioritarie

### Priority 1 (Alto)
- [ ] Migliorare qualità immagini
- [ ] Aggiungere più lingue
- [ ] Fix bug critici
- [ ] Migliorare inclusività

### Priority 2 (Medio)
- [ ] Aggiungere dashboard web
- [ ] Gallery comunità
- [ ] Fine-tuning del modello
- [ ] Webhook integration

### Priority 3 (Basso)
- [ ] Mobile app
- [ ] Integrazioni aggiuntive
- [ ] Performance optimization

---

## 🧪 Testing

### Run tests
```bash
pytest tests/ -v
```

### Coverage report
```bash
pytest --cov=backend tests/
```

### Test structure
```
tests/
├── test_models.py          # Test dei Pydantic models
├── test_prompts.py         # Test prompt generation
├── test_api.py             # Test API endpoints
└── test_inclusivity.py      # Test inclusività
```

### Scrivere test
```python
def test_body_type_validation():
    """Test che obese sia supportato"""
    request = StoryRequest(
        prompt="insegnante",
        body_type="obese",
        skin_tone="dark"
    )
    assert request.body_type == "obese"

def test_negative_keyword_validation():
    """Test che 'fat' venga rifiutato"""
    is_valid, error = validate_prompt("fat person")
    assert not is_valid
    assert "fat" in error.lower()
```

---

## 🚀 Release Process

1. Update version in `backend/main.py`
2. Update CHANGELOG
3. Create GitHub release
4. Deploy to production

---

## 🔗 Links Utili

- [GitHub Issues](https://github.com/tomahawok-source/inclusive-story-bot/issues)
- [GitHub Discussions](https://github.com/tomahawok-source/inclusive-story-bot/discussions)
- [API Docs](./API.md)
- [Setup Guide](./SETUP.md)
- [Inclusivity Guidelines](./INCLUSIVITY.md)

---

## 💖 Principi Comunitari

1. **Rispetto**: Tratta tutti con dignità
2. **Inclusività**: Tutti i contributi sono benvenuti
3. **Transparency**: Comunica apertamente
4. **Accountability**: Ammetti gli errori
5. **Growth**: Impara e cresci insieme

---

## ❓ Domande?

- 📧 Apri un'issue con tag `[QUESTION]`
- 💬 Usa GitHub Discussions
- 🤝 Contatta i maintainer

---

**Grazie per contribuire! Voi rendete questo progetto possibile. ❤️**
