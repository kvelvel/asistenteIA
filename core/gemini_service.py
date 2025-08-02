import os
from config import AppConfig

"""import google.generativeai as genai
from google.generativeai.types import HarmBlockThreshold, HarmCategory"""

from google import genai
from google.genai import types


from errors.exceptions import GeminiServiceError

class GeminiService:
    def __init__(self):
        if not AppConfig.GEMINI_API_KEY:
            raise GeminiServiceError(
                message="La clave de API de Gemini no está configurada.",
                status_code=400
            )
            
        self.client = genai.Client()
        
        """ genai.configure(api_key=AppConfig.GEMINI_API_KEY)
        print(f"Conectado a Gemini con la clave de API: {AppConfig.GEMINI_API_KEY}")
        self.model = genai.GenerativeModel(AppConfig.GEMINI_MODEL_NAME)
        print(f"Conectado a Gemini con el modelo: {AppConfig.GEMINI_MODEL_NAME}")
        print(f"Conectado a Gemini con el modelo: {self.model}") """

    def get_response(self, prompt: str, history: list = None) -> str:
        print(f"este es el modelo: {self.client.models}")
        try:
            """ Configuración de seguridad para bloqueo de contenido,
            puede cambiar para produccion (
                BLOCK_NONE = no bloquea nada,
                BLOCK_LOW_AND_ABOVE = bloquea bajo y superior,
                BLOCK_MEDIUM_AND_ABOVE = bloquea medio y superior,
                BLOCK_HIGH_AND_ABOVE = bloquea alto y superior
            )"""
            safety_settings_project = [
                types.SafetySetting(
              category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
              threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            ),
            types.SafetySetting(
              category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
              threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            ),
            types.SafetySetting(
              category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
              threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            ),
            types.SafetySetting(
              category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
              threshold=types.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            )
            ]
            
            if history:
                print(f"este es el modelo: {self.client.models}")
                
            else:
                print(f"este es el modelo: {self.client.models.list}")
                response = self.client.models.generate_content(
                                model=AppConfig.GEMINI_MODEL_NAME,
                                contents=prompt,
                                config=types.GenerateContentConfig(
                                    safety_settings=safety_settings_project
                                )
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
