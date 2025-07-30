class ApplicationError(Exception):
    """Excepción base para todos los errores de la aplicación."""
    def __init__(
                    self,
                    message="Ocurrió un error en la aplicación.",
                    status_code=500
                ):
        super().__init__(message)
        self.message = message
        self.status_code = status_code


class GeminiServiceError(ApplicationError):
    """Excepción para errores al interactuar con el servicio Gemini."""
    def __init__(
                    self,
                    message="Error al comunicarse con Gemini.",
                    status_code=500
                ):
        super().__init__(message, status_code)
