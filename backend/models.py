"""
Modelli Pydantic per Inclusive Story Bot
"""

from pydantic import BaseModel, Field
from typing import Optional, List

class BodyType(BaseModel):
    value: str
    label: str
    description: str

class SkinTone(BaseModel):
    value: str
    label: str
    hex: str

class StoryRequest(BaseModel):
    """Richiesta per generare una storia"""
    prompt: str = Field(..., description="Descrizione della storia/persona")
    body_type: str = Field(default="average", description="Tipo di corporatura")
    skin_tone: str = Field(default="medium", description="Colore della pelle")
    representation: str = Field(default="diverse, inclusive, respectful", description="Parole chiave di rappresentazione")
    language: str = Field(default="it", description="Lingua dei prompt")

class StoryResponse(BaseModel):
    """Risposta con immagine generata"""
    status: str
    image_base64: str
    prompt_used: str
    body_type: str
    skin_tone: str
    message: str
    generation_time: float
    model: str

class HealthResponse(BaseModel):
    """Response per health check"""
    status: str
    version: str
    model_loaded: bool
    gpu_available: bool
    timestamp: str

class BodyTypesResponse(BaseModel):
    """Response per body types"""
    total: int
    body_types: List[BodyType]

class SkinTonesResponse(BaseModel):
    """Response per skin tones"""
    total: int
    skin_tones: List[SkinTone]
