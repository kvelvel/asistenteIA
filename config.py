import os
from dotenv import load_dotenv

load_dotenv() 
class AppConfig:
    # --- Configuración General ---
    APP_ENV = os.getenv("APP_ENV")
    DEBUG = APP_ENV == "development"

    # --- Configuración de Google Gemini API ---
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME")
    GEMINI_RESPONSE_LENGTH = int(os.getenv("GEMINI_RESPONSE_LENGTH", 100)) 
    
    # --- Configuración de Logger ---
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            },
            'detailed': { 
                'format': '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'standard',
                'level': 'INFO'
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'detailed',
                'filename': 'logs/app.log',
                'maxBytes': 10485760, # 10 MB
                'backupCount': 5, 
                'level': 'WARNING'
            }
        },
        'loggers': {
            '': { 
                'handlers': ['console', 'file'],
                'level': 'DEBUG',
                'propagate': False
            },
            'werkzeug': { 
                'handlers': ['console'],
                'level': 'INFO',
                'propagate': False
            }
        }
    }
