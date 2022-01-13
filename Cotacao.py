#Link da API de consumo > https://docs.awesomeapi.com.br/api-de-moedas

#importações de bibliotecas
import requests
from fastapi import FastAPI

#declaração de variável
app = FastAPI()

#processando a cotacao
@app.get('/cotacao')
def cotacao(de:str="USD", para:str="BRL", valor:float=1):
    #consumindo API
    cotacao = requests.get(f"https://economia.awesomeapi.com.br/last/{de}-{para}")

    #convertendo para json
    cotacao = cotacao.json()

    #processando resultados
    result = float(cotacao[de+para]["bid"]) * valor

    #retornando resultados
    return(cotacao, {"conversao" : result})
