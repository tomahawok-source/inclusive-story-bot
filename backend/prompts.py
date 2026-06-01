"""
Prompt templates per Inclusive Story Bot
"""

INCLUSIVE_PROMPTS = {
    "professional": {
        "it": "CEO/executive che presenta a riunione con autorevolezza e fiducia",
        "en": "CEO/executive presenting at meeting with authority and confidence",
    },
    "teacher": {
        "it": "Insegnante che spiega concetti complessi in classe con passione",
        "en": "Teacher explaining complex concepts in classroom with passion",
    },
    "artist": {
        "it": "Artista che crea un capolavoro nello studio con creatività",
        "en": "Artist creating a masterpiece in studio with creativity",
    },
    "athlete": {
        "it": "Atleta che si allena in palestra con forza e determinazione",
        "en": "Athlete training in gym with strength and determination",
    },
    "doctor": {
        "it": "Medico che visita paziente con cura e competenza",
        "en": "Doctor examining patient with care and expertise",
    },
    "scientist": {
        "it": "Scienziato che conduce ricerca in laboratorio con dedizione",
        "en": "Scientist conducting research in laboratory with dedication",
    },
    "parent": {
        "it": "Genitore che gioca con figli con amore e tenerezza",
        "en": "Parent playing with children with love and tenderness",
    },
    "leader": {
        "it": "Leader che ispira e guida il team con saggezza",
        "en": "Leader inspiring and guiding team with wisdom",
    },
}

BODY_TYPE_DESCRIPTIONS = {
    "slim": {
        "it": "Corporatura snella e elegante",
        "en": "Slim and elegant body type",
    },
    "average": {
        "it": "Corporatura media",
        "en": "Average body type",
    },
    "athletic": {
        "it": "Corporatura atletica e tonica",
        "en": "Athletic and toned body type",
    },
    "chubby": {
        "it": "Corporatura morbida",
        "en": "Soft and gentle body type",
    },
    "obese": {
        "it": "Corporatura obesa - RAPPRESENTAZIONE POSITIVA E RISPETTOSA",
        "en": "Obese body type - POSITIVE AND RESPECTFUL REPRESENTATION",
    },
    "muscular": {
        "it": "Corporatura muscolosa e potente",
        "en": "Muscular and powerful body type",
    },
    "curvy": {
        "it": "Corporatura curvilinea",
        "en": "Curvy body type",
    },
    "androgynous": {
        "it": "Corporatura androgina",
        "en": "Androgynous body type",
    },
    "tall": {
        "it": "Corporatura alta e slanciata",
        "en": "Tall and slender body type",
    },
}

SKIN_TONE_DESCRIPTIONS = {
    "very_light": {
        "it": "Pelle molto chiara",
        "en": "Very light skin",
    },
    "light": {
        "it": "Pelle chiara",
        "en": "Light skin",
    },
    "medium": {
        "it": "Pelle media",
        "en": "Medium skin",
    },
    "tan": {
        "it": "Pelle abbronzata",
        "en": "Tan skin",
    },
    "dark": {
        "it": "Pelle scura",
        "en": "Dark skin",
    },
    "very_dark": {
        "it": "Pelle molto scura",
        "en": "Very dark skin",
    },
}

REPRESENTATION_KEYWORDS = {
    "inclusive": [
        "diverse",
        "inclusive",
        "respectful",
        "empowering",
        "dignified",
        "authentic",
        "positive",
        "beautiful",
    ],
    "style": [
        "professional",
        "well-lit",
        "high quality",
        "portrait",
        "photography",
        "confident",
        "natural",
    ],
}

def build_prompt(base_prompt: str, body_type: str, skin_tone: str, language: str = "en") -> str:
    """
    Costruisce un prompt inclusivo per la generazione di immagini
    """
    body_desc = BODY_TYPE_DESCRIPTIONS.get(body_type, {}).get(language, body_type)
    skin_desc = SKIN_TONE_DESCRIPTIONS.get(skin_tone, {}).get(language, skin_tone)
    
    keywords = " ".join(REPRESENTATION_KEYWORDS["inclusive"])
    
    if language == "it":
        prompt = f"""
        Foto professionale di una persona bellissima con:
        - Corporatura: {body_desc}
        - Colore della pelle: {skin_desc}
        - Azione: {base_prompt}
        - Stile: {keywords}, fotografico, naturale, positivo
        - Qualità: alta qualità, ben illuminata, rispettosa
        """
    else:
        prompt = f"""
        Professional photo of a beautiful person with:
        - Body type: {body_desc}
        - Skin tone: {skin_desc}
        - Action: {base_prompt}
        - Style: {keywords}, photographic, natural, positive
        - Quality: high quality, well-lit, respectful
        """
    
    return prompt.strip()
