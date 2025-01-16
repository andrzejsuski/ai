# Połączenie się przez API z modelem ollama/lamma3.2 

# Import

import os
import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display

# Stałe połączenie się z modelem ollama/llama3.2 

OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "llama3.2"

# Przykładowe wiadomości dla modelu

messages = [
    {"role": "system", "content": "Jesteś nauczycielem"},
    {"role": "user", "content": "Czego najlepiej nauczyć 6 letnie dziecko z matematyki odpowiedz w formacie HTML"}
]
payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }
response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
print(response.json()['message']['content'])
