import requests

def cotacaoDolar():
    url = 'https://api.exchangeratesapi.io/latest?base=USD&symbols=BRL'
    response = requests.get(url)
    dados = response.json()
    cotacao = dados["rates"]["BRL"]
    return cotacao

obtendo_cotacao_dolar = cotacaoDolar()
print(f"A cotação atual do Dólar é de: R$ {obtendo_cotacao_dolar:.2f}")