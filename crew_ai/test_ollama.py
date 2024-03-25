import requests
from decouple import config
from pprint import pprint

# Replace 'http://custom-url-to-ollama.com' with your custom Ollama URL
ollama_url = "http://localhost:11434/api/generate"


# Send a POST request to the Ollama URL with the user input
response = requests.post(ollama_url, json={'model': 'mixtral', 'prompt': 'Respond 2 words', "stream": False}, timeout=60)

# If the request is successful, print the Ollama's response
if response.status_code == 200:
    #ollama_response = response.json()['result']
    pprint(response.json())
else:
    print("Failed to connect to Ollama")