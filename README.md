# servertcp-e-flaskrestfull
Este Repositório trata-se de um projeto simples para utilizar as habilidades de Python e criar uma API Restfull juntamente com um servidor TCP e cliente TCP, com o intuito de por em prática novos conceitos aprendidos.

## Sumário

- [A API](#a-api)
- [O Servidor](#o-servidor)
- [O Banco de Dados](#o-banco-de-dados)
- [Instalando Dependências](#instalando-dependencias)
- [Rodando o Projeto](#rodando-o-projeto)
- [Rotas](#rotas)

## A API

A API é construido com Flask RestFul na qual consulta, altera e adiciona produtos cadastrados e mostra e altera os dados, nome e senha, de cada usuário. Para realizar as consultar pela API é necessário ter um cadastro de usuário e utilizar sua senha como hash, enviando o hash para validar a consulta e o que irá ser consultado.

## O Servidor

O Servidor recebe a consulta da API, compara a hash enviada com a que ele irá gerar através da senha, caso elas sejam iguais, o servidor consulta o banco de dados e envia no formato JSON para a API a resposta.

## O Banco de Dados

O banco de dados foi construído através da ORM SQLAlchemy em SQLite3, na qual possui apenas 2 tabelas, a tabela usuários(users) e a tabela produtos(products)

## Instalando Dependências

Primeiro, clone ou faça o download do repositório

```
git clone https://github.com/fabiobarkoski/servertcp-e-flaskrestfull.git
```

Acesse a pasta
```
cd servertcp-e-flaskrestfull
```

Após acesse o ambiente virtual e instale as dependências
```
myvenv\Scripts\activate
pip install -r requirements.txt
```

## Rodando o projeto

Para rodar o projeto insira em um Terminal/Shell o comando
```
python server.py ou python3 server.py
```
e em outro Terminal/Shell insira o comando
```
python app.py ou python3 app.py
```

## Rotas

As rotas da API são as seguintes

- /'<hash do usuario>'/products/
  Realiza a consulta e retorna todos os produtos, bem como cadastra novos
  
- /'<hash do usuario>'/product/<id do produto>/
  Altera os dados do produto ou exclui ele
  
- /'<hash do usuario>'/ 
  Consulta os dados pessoais do usuário e altera a senha do mesmo
