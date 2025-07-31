import os
from config import AppConfig
from google import genai
from google.genai.types import HarmBlockThreshold, HarmCategory


from errors.exceptions import GeminiServiceError

class GeminiService:
    def __init__(self):
        if not AppConfig.GEMINI_API_KEY:
            raise GeminiServiceError(
                message="La clave de API de Gemini no está configurada.",
                status_code=400
            )
        
        self.client = genai.Client(api_key=AppConfig.GEMINI_API_KEY)
        print(f"Conectado a Gemini")

    def get_response(self, prompt: str, history: list = None) -> str:
        try:
            """ Configuración de seguridad para bloqueo de contenido,
            puede cambiar para produccion (
                BLOCK_NONE = no bloquea nada,
                BLOCK_LOW_AND_ABOVE = bloquea bajo y superior,
                BLOCK_MEDIUM_AND_ABOVE = bloquea medio y superior,
                BLOCK_HIGH_AND_ABOVE = bloquea alto y superior
            )"""
            safety_settings = {
                HarmCategory.HARM_CATEGORY_HATE_SPEECH:
                    HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_HARASSMENT:
                    HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT:
                    HarmBlockThreshold.BLOCK_NONE,
                HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT:
                    HarmBlockThreshold.BLOCK_NONE,
            }

            if history:
                """chat = self.model.start_chat(history=history)
                response = chat.send_message(
                                                prompt,
                                                safety_settings=safety_settings
                                            )""" 
            else:
                response = self.client.models.generate_content(
                                model=AppConfig.GEMINI_MODEL_NAME,
                                contents=prompt
                                #safety_settings=safety_settings
                                )

            if response.candidates:
                response_text = ""
                for part in response.candidates[0].content.parts:
                    if hasattr(part, 'text'):
                        response_text += part.text
                return response_text
            elif (response.prompt_feedback
                    and response.prompt_feedback.block_reason):
                raise GeminiServiceError(
                    message=f"Prompt bloqueado por Gemini: "
                            f"{response.prompt_feedback.block_reason.name}",
                    status_code=403
                )
            else:
                raise GeminiServiceError()

        except Exception as e:
            print(f"Error al conectar con Gemini: {e}")
            raise GeminiServiceError(
                message=(
                            "Error desconocido al obtener una"
                            " respuesta de Gemini.",
                ),
                status_code=500
            ) from e
