import re
import requests

req = requests.get('https://www.hugoboss.com.br/servico-cliente/contato')

string = 'testemail123@example.com'

variavel = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req.text)  #RAW String
#variavel = re.search(r'', string) #Procura por todo o conteudo em grupo. Ex:. Gato, gata, gatões e etc...

if variavel:
    print(variavel)
else:
    print('Nenhuma palavra encontrada!')

#print(variavel.group())
