import os
from dotenv import load_dotenv
from google import genai

# Carga de .env file
load_dotenv()

# paso de API_KEY a GERMINI
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Obtener inpout de usuario a preguntar a gemini
input_text = input("Sobre que quieres saber: \n ")


# "Request a GEMINI "
response = client.models.generate_content(
    model=os.getenv("MODELO"), contents=input_text
)
print(response.text)
