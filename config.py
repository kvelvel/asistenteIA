# asistente_ia_backend/config.py
import os
from dotenv import load_dotenv

load_dotenv() # Carga las variables del archivo .env

class AppConfig:
    # --- Configuración General ---
    APP_ENV = os.getenv("APP_ENV")
    DEBUG = APP_ENV == "development"

    # --- Configuración de Google Gemini API ---
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME")
