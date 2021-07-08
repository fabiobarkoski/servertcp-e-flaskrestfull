from flask import Flask
from flask_restful import Resource, Api
import socket
import hashlib

h = hashlib.sha1()

app = Flask(__name__)
api = Api(app)

#IP e porta do servidor
HOST = '127.0.0.1'
PORT = 80

#fazendo a conexão ao server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Conectado ao server!\n --------------------------------------------------------------')

class products(Resource):
    def get(self,hash):
        #enviando consulta
        message = hash
        s.sendall(message.encode())
        data = s.recv(1024)
        return {'status' : '200',
                'user' : data.decode()}

api.add_resource(products, '/<string:hash>/products/index/')

if __name__ == '__main__':
    app.run()