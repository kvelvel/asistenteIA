# asistente_ia_backend/errors/handlers.py
from flask import jsonify
from errors.exceptions import ApplicationError
import logging

# Configuración básica de logging (se puede mejorar con config.py)
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def handle_application_error(e: ApplicationError):
    """
    Maneja las excepciones personalizadas de la aplicación.
    Devuelve una respuesta JSON con el mensaje y el código de estado apropiado.
    """
    logger.error(f"Application Error: {e.status_code} - {e.message}", exc_info=True)
    response = jsonify({
        "error": e.message,
        "code": e.status_code
    })
    response.status_code = e.status_code
    return response

def handle_validation_error(e):
    """
    Maneja errores de validación (ej. de frameworks como Marshmallow o Pydantic).
    Un ejemplo para BadRequest que Flask lanza.
    """
    logger.error(f"Validation Error: {e.description}", exc_info=True)
    response = jsonify({
        "error": "Datos de entrada inválidos",
        "details": e.description # Esto puede variar según el validador
    })
    response.status_code = 400
    return response

def handle_generic_exception(e):
    """
    Maneja cualquier excepción no esperada.
    Devuelve un error genérico y registra la excepción completa.
    """
    logger.critical(f"Unhandled Exception: {e}", exc_info=True)
    response = jsonify({
        "error": "Ocurrió un error inesperado en el servidor.",
        "code": 500
    })
    response.status_code = 500
    return response