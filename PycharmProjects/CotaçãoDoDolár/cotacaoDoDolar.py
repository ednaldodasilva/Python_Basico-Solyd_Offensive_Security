import datetime
import json
import time

import requests

req = requests.get('https://economia.awesomeapi.com.br/json/daily/:moeda/:numero_dias')

cotacao = json.loads(req.text)
print(cotacao['numero_dias']['USD-BRL'])

print('Cotação', datetime.datetime.now())
time.sleep(2)