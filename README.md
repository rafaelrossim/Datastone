- Solicitação
Construa uma API, que responda JSON, para conversão monetária. Ela deve ter uma moeda de lastro (USD) e fazer conversões entre diferentes moedas com cotações de verdade e atuais. A API deve, originalmente, converter entre as seguintes moedas (USD, BRL, EUR, BTC, ETH)

- Requisitos
O código precisa rodar em Linux Ubuntu (preferencialmente como container Docker)
Para executar seu código, deve ser preciso apenas rodar os seguintes comandos:
git clone $seu-fork
cd $seu-fork
comando para instalar dependências
comando para executar a aplicação
A API pode ser escrita com ou sem a ajuda de frameworks (À sua escolha)

- Solução
O problema em questão foi solucionado consumindo a api da awesomeapi (https://docs.awesomeapi.com.br/api-de-moedas), 
porém houve a necessidade de converter para json conforme requisitado pois a resposta da api é apenas (200 ou 400).

