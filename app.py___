#Archivo de prueba de flask
from flask import Flask

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define una "ruta" o URL para tu aplicación
@app.route('/')
def hola_mundo():
    return '¡Hola, mundo desde Flask!'

# Si este archivo se ejecuta directamente, inicia el servidor
if __name__ == '__main__':
    app.run(debug=True) # debug=True te ayuda a ver errores mientras desarrollas