from flask import Blueprint, request, jsonify, Response
from core.ia_facade import IAFacade
from errors.exceptions import InvalidInputError, ApplicationError
from werkzeug.exceptions import BadRequest
import io
import logging

logger = logging.getLogger(__name__) 
api_ia = Blueprint('api_ia', __name__)
facade = IAFacade()

"""@api_bp.route('/dialog', methods=['POST'])
def dialog_endpoint():
    
    Endpoint principal para la interacción de voz con el asistente.
    Recibe un archivo de audio del usuario y devuelve la respuesta del asistente en audio.
    
    if 'audio' not in request.files:
        logger.error("API: Solicitud /dialog sin archivo de audio.")
        raise InvalidInputError("No se proporcionó un archivo de audio.")

    audio_file = request.files['audio']
    
    try:
        audio_data = audio_file.read()
    except Exception as e:
        logger.error(f"API: Error al leer archivo de audio en /dialog: {e}", exc_info=True)
        raise ApplicationError("Error al procesar el archivo de audio.")

    logger.info(f"API: Recibido audio de {len(audio_data)} bytes en /dialog.")

    try:
        response_audio_bytes = facade.process_voice_command(audio_data)
    except ApplicationError as e: # Captura solo tus errores de aplicación
        raise e # Relanza para que el manejador global los capture
    except Exception as e:
        logger.critical(f"API: Error inesperado en IAFacade.process_voice_command: {e}", exc_info=True)
        raise ApplicationError("Error interno al procesar comando de voz.")

    if response_audio_bytes:
        return Response(response_audio_bytes, mimetype="audio/wav")
    else:
        # Esto debería ser manejado por las excepciones, pero como fallback
        raise ApplicationError("No se pudo generar la respuesta de audio final.")"""


@api_ia.route('/text_dialog', methods=['POST'])
def text_dialog_endpoint():
    """
    Endpoint para la interacción de texto con el asistente.
    Recibe un JSON con 'text' y devuelve la respuesta del asistente en texto como JSON.
    """
    data = request.json 
    if not data or 'text' not in data:
        logger.error("API: Solicitud /text_dialog sin JSON o sin clave 'text'.")
        raise InvalidInputError("Se espera un cuerpo JSON con la clave 'text'.")

    user_text = data['text']
    logger.info(f"API: Recibido texto: '{user_text}' en /text_dialog.")

    try:
        response_text = facade.process_text_command(user_text)
        return jsonify({"response": response_text}), 200
    except ApplicationError as e: 
        raise e 
    except Exception as e:
        logger.critical(f"API: Error inesperado en IAFacade.process_text_command: {e}", exc_info=True)
        raise ApplicationError("Error interno al procesar comando de texto.")

"""@api_bp.route('/emergency_alert', methods=['POST'])
# ... (resto de tus rutas) ...
def emergency_alert_endpoint():
    data = request.json
    senior_id = data.get('senior_id')
    message = data.get('message', 'Alerta de emergencia activada.')

    if not senior_id:
        raise InvalidInputError("ID de adulto mayor es requerido.")

    try:
        success = facade.send_emergency_alert(senior_id, message)
        if success:
            return jsonify({"message": "Alerta de emergencia enviada exitosamente"}), 200
        else:
            raise ApplicationError("Fallo al enviar la alerta de emergencia.")
    except ApplicationError as e:
        raise e
    except Exception as e:
        logger.critical(f"API: Error en emergency_alert_endpoint: {e}", exc_info=True)
        raise ApplicationError("Error interno al procesar alerta de emergencia.")

@api_bp.route('/set_reminder', methods=['POST'])
def set_reminder_endpoint():
    data = request.json
    senior_id = data.get('senior_id')
    reminder_details = data.get('reminder_details')

    if not senior_id or not reminder_details:
        raise InvalidInputError("senior_id y reminder_details son requeridos.")

    try:
        message = facade.set_senior_reminder(senior_id, reminder_details)
        return jsonify({"message": message}), 200
    except ApplicationError as e:
        raise e
    except Exception as e:
        logger.critical(f"API: Error en set_reminder_endpoint: {e}", exc_info=True)
        raise ApplicationError("Error interno al establecer recordatorio.")

@api_bp.route('/family_message', methods=['POST'])
def family_message_endpoint():
    data = request.json
    senior_id = data.get('senior_id')
    message = data.get('message')

    if not senior_id or not message:
        raise InvalidInputError("senior_id y message son requeridos.")

    try:
        success = facade.send_family_message_to_senior(senior_id, message)
        if success:
            return jsonify({"message": "Mensaje enviado a la familia del adulto mayor"}), 200
        else:
            raise ApplicationError("Fallo al enviar mensaje a la familia.")
    except ApplicationError as e:
        raise e
    except Exception as e:
        logger.critical(f"API: Error en family_message_endpoint: {e}", exc_info=True)
        raise ApplicationError("Error interno al enviar mensaje familiar.")

@api_bp.route('/preferences/<string:senior_id>', methods=['GET'])
def get_preferences_endpoint(senior_id: str):
    try:
        preferences = facade.get_senior_preferences(senior_id)
        return jsonify(preferences), 200
    except ApplicationError as e:
        raise e
    except Exception as e:
        logger.critical(f"API: Error en get_preferences_endpoint: {e}", exc_info=True)
        raise ApplicationError("Error al obtener preferencias.")"""