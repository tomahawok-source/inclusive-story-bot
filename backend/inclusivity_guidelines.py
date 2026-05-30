"""
Linee guida per la rappresentazione inclusiva e il rispetto della dignità delle persone
Questo modulo definisce i principi etici del progetto
"""

from enum import Enum
from typing import List, Dict

# ============================================================================
# PRINCIPI FONDAMENTALI
# ============================================================================

CORE_PRINCIPLES = """
🌟 PRINCIPI FONDAMENTALI DI INCLUSIVITÀ

1. DIGNITÀ UNIVERSALE
   - Ogni corpo è un corpo. Punto.
   - La dignità non dipende da come una persona appare
   - Tutte le corporature meritano rispetto e rappresentazione

2. NESSUNO STEREOTIPO
   - NO: "Le persone obese sono pigre"
   - SÌ: "Le persone obese sono capaci, intelligenti, talentuose come chiunque altro"
   
3. CELEBRAZIONE DELLA DIVERSITÀ
   - La diversità NON è un problema da risolvere
   - La diversità è bellezza, unicità, ricchezza

4. VISIBILITÀ E RAPPRESENTAZIONE
   - Evitare l'invisibilizzazione (affatto token)
   - Mostrare persone diverse in TUTTI i ruoli e contesti
   - Nessun "ruolo predefinito" per un tipo di corpo

5. LINGUAGGIO CONSAPEVOLE
   - Usare termini neutri e rispettosi
   - Evitare diminutivi o infantilizzazione
   - Evitare pity-framing ("nonostante il suo corpo...")
"""

# ============================================================================
# CORPORATURE - LINEE GUIDA SPECIFICHE
# ============================================================================

BODY_TYPE_GUIDELINES = {
    "obese": {
        "positive_contexts": [
            "Professionisti di successo (CEO, medici, avvocati, insegnanti)",
            "Artisti e creativi appassionati",
            "Genitori amorevoli e dediti",
            "Atleti e sportivi",
            "Leader carismatici",
            "Persone confident e happy",
            "Modelle e fashion icon",
            "Persone in situazioni non relate al corpo"
        ],
        "keywords_to_use": [
            "beautiful", "confident", "capable", "powerful", "talented",
            "respected", "dignified", "intelligent", "warm", "loving",
            "elegant", "graceful", "happy", "comfortable", "valued"
        ],
        "keywords_to_avoid": [
            "fat", "unhealthy", "lazy", "unattractive", "out of shape",
            "problematic", "sad", "ashamed", "burden", "burden on"
        ],
        "context_rules": [
            "NOT every story deve essere about weight",
            "NOT every story deve essere about diet/fitness",
            "Non mostrare SOLO persone obese in contesti di food o eating",
            "Se è healthcare, mostra RESPECTFUL treatment, non bias"
        ]
    }
}

# ============================================================================
# ANTI-PATTERNS - COSA NON FARE
# ============================================================================

ANTI_PATTERNS = {
    "Body-related": {
        "❌ DON'T": "Show obese people only in food/eating contexts",
        "✅ DO": "Show obese people in ALL contexts equally",
        "❌ DON'T": "Use before/after weight loss narratives",
        "✅ DO": "Show people happy at their current size",
        "❌ DON'T": "Associate obesity with laziness, stupidity, sadness",
        "✅ DO": "Show obese people as intelligent, capable, confident",
    },
    
    "Skin-tone-related": {
        "❌ DON'T": "Only show dark skin in non-leadership roles",
        "✅ DO": "Show dark skin in equal proportion in leadership",
        "❌ DON'T": "Use 'exotic' for non-white skin tones",
        "✅ DO": "Describe all skin tones as beautiful",
    },
    
    "General": {
        "❌ DON'T": "Use inspiration porn / pity narratives",
        "✅ DO": "Treat all people as regular humans, not inspirational",
        "❌ DON'T": "Create tokenistic diverse characters",
        "✅ DO": "Integrate diversity naturally across all content",
    }
}

# ============================================================================
# MANIFESTO
# ============================================================================

INCLUSIVITY_MANIFESTO = """
╔════════════════════════════════════════════════════════════════╗
║           INCLUSIVE STORY BOT - MANIFESTO DI INCLUSIVITÀ        ║
╚════════════════════════════════════════════════════════════════╝

Noi crediamo che:

🌈 NESSUN CORPO È SBAGLIATO
   Ogni corpo è un corpo valido. Questo bot rappresenta TUTTE le corporature
   con uguale dignità, bellezza e rispetto.

👥 LA DIVERSITÀ È FORZA
   Mostriamo persone diverse in TUTTI i ruoli, contesti e situazioni.
   Leader, artisti, insegnanti, genitori - di OGNI forma e colore.

💪 IL CORPO NON DEFINE IL VALORE
   La corporatura di una persona non determina le sue capacità, intelligenza,
   bellezza, valore o diritto a essere rappresentata.

🚫 NIENTE STEREOTIPI
   Niente associazioni corpo-pigrizia, corpo-stupiditá, peso-malattia.
   Niente pity narratives. Solo umanità e dignità.

✨ RAPPRESENTAZIONE UGUALE = PREGIUDIZI MINORI
   Quando vediamo diverse corporature e persone in posizioni di potere,
   gli stereotipi diminuiscono.

🤝 COMUNITÀ SOPRA TUTTO
   Questo è fatto per le persone discriminate per il loro corpo.
   Le vostre voci, i vostri feedback, le vostre storie guidano questo progetto.

---
Questo bot è uno strumento per l'empowerment e l'abbattimento dei pregiudizi.
Ogni immagine generata è un atto di resistenza contro la marginalizzazione.

Con ❤️ e dignità,
Il Team di Inclusive Story Bot
"""

def get_inclusive_guidelines_for_body_type(body_type: str) -> Dict:
    """Restituisce le linee guida specifiche per un tipo di corporatura"""
    return BODY_TYPE_GUIDELINES.get(body_type, {})


def validate_against_guidelines(prompt: str, body_type: str) -> List[str]:
    """
    Valida un prompt contro le linee guida di inclusività.
    
    Returns:
        Lista di warning se presenti, vuota se tutto è OK
    """
    warnings = []
    prompt_lower = prompt.lower()
    
    # Check for negative keywords
    negative_keywords = BODY_TYPE_GUIDELINES.get(body_type, {}).get("keywords_to_avoid", [])
    for keyword in negative_keywords:
        if keyword.lower() in prompt_lower:
            warnings.append(f"⚠️ Evita '{keyword}' - usa termini più rispettosi")
    
    return warnings
