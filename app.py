from flask import Flask
from flask_restful import Resource, Api
import socket
import hashlib

h = hashlib.sha1()

app = Flask(__name__)
api = Api(app)

HOST = '127.0.0.1'
PORT = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Conectado ao server!\n --------------------------------------------------------------')

class index(Resource):
    def get(self,hash):
        
        h.update(hash.encode())
        print(h.hexdigest())
        message = hash
        s.sendall(message.encode())
        data = s.recv(1024)
        return {'status' : '200',
                'user' : data.decode()}

api.add_resource(index, '/<string:hash>/index/')

if __name__ == '__main__':
    app.run()