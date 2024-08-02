import requests
import json

tempo = input('Qual a cidade você deseja ver o tempo: ')

api = requests.get('https://api.hgbrasil.com/weather', tempo)

clima = json.loads(api.text)

print(clima)
