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
        message = json.dumps({'method': 'POST',
                              'hash': hash,
                              'to': 'products',
                              'name': dataSend['name'],
                              'type': dataSend['type'],
                              'amount': dataSend['amount']})
        s.sendall(message.encode())
        data = s.recv(1024)
        return json.loads(data.decode())


class product(Resource):
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
        # recebendo resposta
        data = s.recv(1024)
        return json.loads(data.decode())


class user(Resource):
    def get(self, hash):
        # enviando consulta
        message = json.dumps({'method': 'GET',
                              'hash': hash,
                              'to': 'users'})
        s.sendall(message.encode())
        # recebendo resposta
        data = s.recv(1024)
        return json.loads(data.decode())

    def put(self, hash):
        dataSend = request.json
        message = json.dumps({'method': 'PUT',
                              'hash': hash,
                              'to': 'users',
                              'password': dataSend['password']})
        s.sendall(message.encode())
        # recebendo resposta
        data = s.recv(1024)
        return json.loads(data.decode())


# consulta todos os produtos e cadastra novos
api.add_resource(products, '/<string:hash>/products/')
api.add_resource(product, '/<string:hash>/product/<int:id>/')
# consulta os dados pessoais do usuário
api.add_resource(user, '/<string:hash>/')

if __name__ == '__main__':
    app.run()
