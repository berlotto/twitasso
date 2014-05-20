Twitasso
===

É um simples aplicativo que lê uma lista de twitts (twitts.txt), organizados linha a linha, e fica postando no Twitter periodicamente.

Como utilizar
---

Primeiro baixe o código: 

`git clone https://github.com/berlotto/twitasso.git`

`cd twitasso`

Instale as dependências (recomendo utilizar o virtualenv): 

`pip install -r requirements.txt`

Crie uma app no seu twitter, em http://dev.twitter.com

Ajuste as variaveis necessárias:

__tempo__: em seguntos, tempo de espera entre um twitt e outro.

__app_key__, __app_secret__, __oauth_token__, __oauth_token_secret__: Dados de acesso da aplicação criada no Twitter.

Abra o arquivo twitts.txt e adicione todos os twitts que você quer se sejam postados.

Agora, só rodar o script:

`python twitasso.py`

... e acompanhar seu twitter !

