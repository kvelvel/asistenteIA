from flask import Flask

from blueprints.api.routes import api_ia

from config import AppConfig
from errors.exceptions import ApplicationError, InvalidInputError, GeminiServiceError
from errors.handlers import handle_application_error, handle_validation_error, handle_generic_exception
from werkzeug.exceptions import BadRequest
import logging
import logging.config

logging.config.dictConfig(AppConfig.LOGGING_CONFIG)
logger = logging.getLogger(__name__)


app = Flask(__name__)
app.config['DEBUG'] = AppConfig.DEBUG

app.register_blueprint(api_ia, url_prefix='/ia')


# Registro de Manejadores de Errores (estos son globales para toda la aplicación)
app.register_error_handler(ApplicationError, handle_application_error)
app.register_error_handler(BadRequest, handle_validation_error)
app.register_error_handler(Exception, handle_generic_exception)

@app.route('/')
def health_check():
    logger.info("Health check endpoint accessed.")
    return "Asistente IA Backend está activo y funcionando."

if __name__ == '__main__':
    logger.info("Iniciando servidor Flask con múltiples Blueprints...")
    app.run(host='0.0.0.0', port=5001, debug=AppConfig.DEBUG)
