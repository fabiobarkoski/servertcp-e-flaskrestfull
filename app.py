from flask import Flask, request
from flask_restful import Resource, Api
import socket
import json

app = Flask(__name__)
api = Api(app)

# IP e porta do servidor
HOST = '127.0.0.1'
PORT = 80

# Fazendo a conexão ao server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Conectado ao server!\n ------------------------------')


class products(Resource):
    """
    Classe da rota produtos da qual exibi todos e cadastra novos
    """

    def get(self, hash):
        # enviando consulta
        message = json.dumps({'method': 'GET',
                              'hash': hash,
                              'to': 'products'})
        s.sendall(message.encode())
        # recebendo resposta
        data = s.recv(1024)
        return json.loads(data.decode())

    def post(self, hash):
        dataSend = request.json
# conversão de dicionario para JSON
        message = json.dumps({'method': 'POST',
                              'hash': hash,
                              'to': 'products',
                              'name': dataSend['name'],
                              'type': dataSend['type'],
                              'amount': dataSend['amount']})
        s.sendall(message.encode())
        data = s.recv(1024)
# conversão de JSON para python
        return json.loads(data.decode())


class product(Resource):
    """
    Classe da rota produto da qual altera
    os dados e exclui um produto em especifico
    """

    def put(self, hash, id):
        dataSend = request.json
        message = json.dumps({'method': 'PUT',
                              'hash': hash,
                              'to': 'products',
                              'id': id,
                              'name': dataSend['name'],
                              'type': dataSend['type'],
                              'amount': dataSend['amount']})
        s.sendall(message.encode())
        data = s.recv(1024)
        return json.loads(data.decode())

    def delete(self, hash, id):
        message = json.dumps({'method': 'DELETE',
                              'hash': hash,
                              'to': 'products',
                              'id': id})
        s.sendall(message.encode())
        data = s.recv(1024)
        return json.loads(data.decode())


class user(Resource):
    """
    Classe da rota usuário na qual exibe as informações
    do usuário que esta consultando e os altera
    """

    def get(self, hash):
        message = json.dumps({'method': 'GET',
                              'hash': hash,
                              'to': 'users'})
        s.sendall(message.encode())
        data = s.recv(1024)
        return json.loads(data.decode())

    def put(self, hash):
        dataSend = request.json
        message = json.dumps({'method': 'PUT',
                              'hash': hash,
                              'to': 'users',
                              'password': dataSend['password']})
        s.sendall(message.encode())
        data = s.recv(1024)
        return json.loads(data.decode())


# consulta todos os produtos e cadastra novos, métodos GET e POST
api.add_resource(products, '/<string:hash>/products/')
# altera e exclui produto do banco de dados, métodos PUT e DELETE
api.add_resource(product, '/<string:hash>/product/<int:id>/')
# consulta os dados pessoais do usuário e os altera, método GET e POST
api.add_resource(user, '/<string:hash>/')

if __name__ == '__main__':
    app.run()
