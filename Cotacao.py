#Link da API de consumo > https://docs.awesomeapi.com.br/api-de-moedas

#importações de bibliotecas
import requests
from fastapi import FastAPI

#declaração de variável
app = FastAPI()

#processando a cotacao
@app.get('/cotacao')
def cotacao(de:str, para:str, valor:float):
    #consumindo API
    cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,USD-EUR,BTC-USD,ETH-USD")

    #convertendo para json
    cotacao = cotacao.json()

    #processando resultados
    cot = cotacao[de+para]
    result = float(cotacao[de+para]["bid"]) * valor

    #retornando resultados
    return(cot, {"conversao" : result})
