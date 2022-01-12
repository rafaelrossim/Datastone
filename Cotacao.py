#importações de bibliotecas
import requests

#consumindo a API
cot = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,USD-EUR,BTC-USD,ETH-USD")

#convertendo para json
cot = cot.json()

#printando o valor
print(cot)

#extra - dolar atual
cot_d = cot['USDBRL']['bid']
print(f'O valor atual do Dólar é ${cot_d:.4}')
