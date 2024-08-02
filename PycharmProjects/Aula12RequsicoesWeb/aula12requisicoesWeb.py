import requests

cabecalho = {'USER-Agent':'Windows 11','Referer':'https://hackersfailed.com','CF-IPCountry':'LS'}

cookies = {'Ultimo-Acesso':'17-01-24'}

dados = {'username':'Ednaldinho','password':'ednaldinhojr0103'}

texto = None
try:
    requisicao = requests.get('https://putsreq.com/oaekeMYu3wrgblAgvAcv', headers=cabecalho, cookies=cookies, data=dados)
    texto = requisicao.text
except Exception as i:
    print("A requisição Web deu erro!", i)

#requisicao = requests.post('https://google.com.br')
#requisicao = requests.delete('https://google.com.br')
#print(type(requisicao))

print(texto)