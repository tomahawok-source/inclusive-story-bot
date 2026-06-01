"""
Inclusive Story Bot - Main API Server
FastAPI backend per generare storie inclusive con immagini
"""

import os
import json
import base64
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import torch
from diffusers import StableDiffusionPipeline

# Configurazione logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Modelli Pydantic
class StoryRequest(BaseModel):
    prompt: str = Field(..., description="Descrizione della storia/persona")
    body_type: str = Field(default="average", description="Tipo di corporatura")
    skin_tone: str = Field(default="medium", description="Colore della pelle")
    representation: str = Field(default="diverse, inclusive, respectful", description="Parole chiave di rappresentazione")
    language: str = Field(default="it", description="Lingua dei prompt")

class StoryResponse(BaseModel):
    status: str
    image_base64: str
    prompt_used: str
    body_type: str
    skin_tone: str
    message: str
    generation_time: float
    model: str

# Corpo types e skin tones
BODY_TYPES = {
    "slim": {"label": "Magra", "description": "Corporatura snella"},
    "average": {"label": "Media", "description": "Corporatura media"},
    "athletic": {"label": "Atletica", "description": "Corporatura atletica"},
    "chubby": {"label": "Morbida", "description": "Corporatura morbida"},
    "obese": {"label": "Obesa", "description": "Corporatura obesa - RAPPRESENTAZIONE POSITIVA"},
    "muscular": {"label": "Muscolosa", "description": "Corporatura muscolosa"},
    "curvy": {"label": "Curvilinea", "description": "Corporatura curvilinea"},
    "androgynous": {"label": "Androgina", "description": "Corporatura androgina"},
    "tall": {"label": "Alta", "description": "Corporatura alta"},
}

SKIN_TONES = {
    "very_light": {"label": "Molto chiara", "hex": "#FDBCB4"},
    "light": {"label": "Chiara", "hex": "#F3D5B5"},
    "medium": {"label": "Media", "hex": "#E0AC69"},
    "tan": {"label": "Abbronzata", "hex": "#C68642"},
    "dark": {"label": "Scura", "hex": "#8D5524"},
    "very_dark": {"label": "Molto scura", "hex": "#614033"},
}

# Inizializzazione FastAPI
app = FastAPI(
    title="Inclusive Story Bot API",
    description="Genera storie e immagini inclusive di persone con diverse corporature e colori di pelle",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Monta la cartella frontend come file statici
frontend_path = Path(__file__).parent.parent / "frontend"
if frontend_path.exists():
    app.mount("/frontend", StaticFiles(directory=str(frontend_path)), name="frontend")
    logger.info(f"✅ Frontend montato da: {frontend_path}")
else:
    logger.warning(f"⚠️  Cartella frontend non trovata: {frontend_path}")

# Modello AI globale
pipe = None

def init_model():
    """Carica il modello Stable Diffusion"""
    global pipe
    try:
        logger.info("📦 Caricamento modello Stable Diffusion...")
        
        # Usa CPU se CUDA non disponibile
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"🖥️  Device: {device}")
        
        # Carica il modello
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            use_auth_token=os.getenv("HUGGINGFACE_TOKEN", None)
        )
        
        pipe = pipe.to(device)
        
        if device == "cpu":
            pipe.enable_attention_slicing()
        
        logger.info("✅ Modello caricato con successo!")
        return True
    except Exception as e:
        logger.error(f"❌ Errore nel caricamento modello: {e}")
        return False

def build_inclusive_prompt(base_prompt: str, body_type: str, skin_tone: str, representation: str) -> str:
    """Costruisce un prompt inclusivo e rispettoso"""
    
    body_desc = BODY_TYPES.get(body_type, {}).get("label", body_type)
    skin_desc = SKIN_TONES.get(skin_tone, {}).get("label", skin_tone)
    
    inclusive_prompt = f"""
    A professional photo of a beautiful person with:
    - Body type: {body_desc}
    - Skin tone: {skin_desc}
    - Doing: {base_prompt}
    - Style: {representation}, professional, dignified, empowering
    - Photography: high quality, well-lit, respectful
    """
    
    return inclusive_prompt.strip()

@app.on_event("startup")
async def startup_event():
    """Inizializza il modello all'avvio"""
    logger.info("🚀 Avvio Inclusive Story Bot...")
    if init_model():
        logger.info("✅ Bot pronto!")
    else:
        logger.error("❌ Errore nell'inizializzazione")

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "name": "Inclusive Story Bot API",
        "version": "1.0.0",
        "description": "Genera storie inclusive con immagini",
        "docs": "/docs",
        "health": "/health",
        "frontend": "/frontend/index.html"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "model_loaded": pipe is not None,
        "gpu_available": torch.cuda.is_available(),
        "timestamp": datetime.now().isoformat()
    }

@app.get("/body-types")
async def get_body_types():
    """Ritorna la lista di corporature supportate"""
    return {
        "total": len(BODY_TYPES),
        "body_types": [
            {"value": key, "label": data["label"], "description": data["description"]}
            for key, data in BODY_TYPES.items()
        ]
    }

@app.get("/skin-tones")
async def get_skin_tones():
    """Ritorna la lista di colori di pelle supportati"""
    return {
        "total": len(SKIN_TONES),
        "skin_tones": [
            {"value": key, "label": data["label"], "hex": data["hex"]}
            for key, data in SKIN_TONES.items()
        ]
    }

@app.post("/generate-story", response_model=StoryResponse)
async def generate_story(request: StoryRequest):
    """Genera una storia con immagine inclusiva"""
    
    if pipe is None:
        raise HTTPException(status_code=503, detail="Modello non caricato")
    
    # Validazione
    if request.body_type not in BODY_TYPES:
        raise HTTPException(status_code=400, detail=f"Body type non valido: {request.body_type}")
    
    if request.skin_tone not in SKIN_TONES:
        raise HTTPException(status_code=400, detail=f"Skin tone non valido: {request.skin_tone}")
    
    try:
        logger.info(f"🎨 Generazione: {request.body_type} - {request.skin_tone}")
        
        # Costruisci prompt inclusivo
        prompt = build_inclusive_prompt(
            request.prompt,
            request.body_type,
            request.skin_tone,
            request.representation
        )
        
        # Genera immagine
        import time
        start_time = time.time()
        
        with torch.no_grad():
            image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]
        
        generation_time = time.time() - start_time
        
        # Converti a base64
        import io
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        image_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        # Salva localmente
        output_dir = Path("generated_images")
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / f"story_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        image.save(output_path)
        
        logger.info(f"✅ Immagine generata: {output_path}")
        
        return StoryResponse(
            status="success",
            image_base64=image_base64,
            prompt_used=prompt,
            body_type=request.body_type,
            skin_tone=request.skin_tone,
            message=f"✅ Storia generata con rappresentazione di corpo {BODY_TYPES[request.body_type]['label'].lower()}",
            generation_time=generation_time,
            model="stabilityai/stable-diffusion-v1-5"
        )
    
    except Exception as e:
        logger.error(f"❌ Errore nella generazione: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/generate-scenario")
async def generate_scenario(
    body_type: str = "obese",
    skin_tone: str = "dark",
    scenario: str = "professional"
):
    """Genera uno scenario predefinito"""
    
    scenarios = {
        "professional": "CEO/executive in a boardroom presenting to team",
        "teacher": "Teacher explaining a complex concept in classroom",
        "artist": "Artist painting a masterpiece in studio",
        "athlete": "Athlete training at the gym with confidence",
        "doctor": "Doctor examining patient with care and expertise",
        "scientist": "Scientist conducting research in laboratory",
    }
    
    prompt = scenarios.get(scenario, scenarios["professional"])
    
    request = StoryRequest(
        prompt=prompt,
        body_type=body_type,
        skin_tone=skin_tone,
        representation="diverse, inclusive, respectful, empowering"
    )
    
    return await generate_story(request)

if __name__ == "__main__":
    import uvicorn
    
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    logger.info(f"🚀 Starting server on {host}:{port}")
    uvicorn.run(app, host=host, port=port)
