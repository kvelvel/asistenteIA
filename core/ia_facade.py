import logging
from errors.exceptions import ApplicationError, GeminiServiceError, InvalidInputError
from core.gemini_service import GeminiService

logger = logging.getLogger(__name__)

class IAFacade:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(IAFacade, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            logger.info("Inicializando IAFacade y sus servicios...")
            self.gemini_service = GeminiService()
            self._initialized = True
            logger.info("IAFacade inicializado.")

    """def process_voice_command(self, audio_data: bytes) -> bytes:
        try:
            logger.info("Facade: Transcribiendo audio...")
            transcribed_text = self.speech_service.transcribe_audio(audio_data)
            if not transcribed_text:
                logger.warning("Facade: No se pudo transcribir audio. Lanzando InvalidInputError.")
                # Lanzar InvalidInputError porque el audio no es procesable
                raise InvalidInputError("No se pudo entender lo que dijiste. Por favor, habla más claro.")

            logger.info(f"Facade: Texto transcrito: '{transcribed_text}'")

            logger.info("Facade: Obteniendo respuesta de Gemini...")
            llm_response_text = self.gemini_service.get_response(transcribed_text)
            if not llm_response_text:
                logger.warning("Facade: Gemini no generó respuesta. Esto debería ser manejado por GeminiServiceError.")
                # Esto es un fallback, GeminiServiceError ya debería ser lanzado por GeminiService
                raise GeminiServiceError("La IA no pudo generar una respuesta significativa.")

            logger.info(f"Facade: Respuesta generada por IA: '{llm_response_text}'")

            logger.info("Facade: Sintetizando respuesta a voz...")
            response_audio = self.speech_service.synthesize_speech(llm_response_text)
            if not response_audio:
                logger.error("Facade: No se pudo sintetizar voz. Error.")
                raise SpeechServiceError("Fallo al sintetizar la respuesta de voz.")

            logger.info("Facade: Proceso de comando de voz completado.")
            return response_audio
        except (SpeechServiceError, GeminiServiceError, InvalidInputError) as e:
            # Captura errores específicos de los servicios o de entrada inválida y los relanza
            logger.error(f"Facade: Error controlado en el procesamiento del comando de voz: {e}", exc_info=True)
            raise e # Relanza la misma excepción para que Flask la capture
        except Exception as e:
            # Captura cualquier otra excepción inesperada en la fachada
            logger.critical(f"Facade: Error inesperado durante el procesamiento del comando de voz: {e}", exc_info=True)
            raise ApplicationError("Un error interno inesperado ocurrió durante el procesamiento del comando de voz.") from e
"""
    def process_text_command(self, text_input: str) -> str:
        logger.info(f"Facade: Procesando comando de texto: '{text_input}'")
        if not text_input or not isinstance(text_input, str):
            raise InvalidInputError(
                message="Entrada de texto inválida. Por favor, proporciona un texto válido.",
                status_code=400
            )
        try:
            response_text = self.gemini_service.get_response(text_input)
            if not response_text:
                logger.warning("Facade: Gemini no respondió a la solicitud de texto. Fallback.")
                return "Lo siento, no pude procesar tu solicitud."

            logger.info(f"Facade: Respuesta de texto generada: '{response_text}'")
            return response_text
        except GeminiServiceError as e:
            logger.error(f"Facade: Error al procesar comando de texto con Gemini: {e}", exc_info=True)
            raise e 
        except InvalidInputError as e:
            logger.warning(f"Facade: Error de entrada inválida: {e.message}", exc_info=True)
            raise e
        except Exception as e:
            logger.critical(f"Facade: Error inesperado al procesar comando de texto: {e}", exc_info=True)
            raise ApplicationError("Un error interno inesperado ocurrió al procesar tu solicitud de texto.") from e

    def send_emergency_alert(self, senior_id: str, message: str) -> bool:
        """
        Envía una alerta de emergencia a los contactos designados.
        """

    def set_senior_reminder(self, senior_id: str, reminder_details: dict) -> str:
        """
        Establece un recordatorio para el adulto mayor.
        """

    def send_family_message_to_senior(self, senior_id: str, message: str) -> bool:
        """
        Guarda un mensaje de la familia para que el asistente lo lea al senior.
        """

    def get_senior_preferences(self, senior_id: str) -> dict:
        """
        Obtiene las preferencias del adulto mayor.
        """