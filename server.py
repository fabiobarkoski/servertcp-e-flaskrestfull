import socket
from models import Users
import hashlib

#IP e porta do servidor
HOST = '127.0.0.1' 
PORT = 80

#criando o socket do server TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server Rodando!')
s.bind((HOST, PORT))
#esperando conexao de cliente
s.listen()
conn, addr = s.accept()
print('Conectado por: ', addr)
#loopíng de receber dados, checar, consultar banco de dados e enviar
while True:
    data = conn.recv(1024)
    if not data:
        break
    datad = data.decode()
    print(f'{datad} enviado de:  + {addr}')
    message = None
    userAll = Users.query.all()
    for user in userAll:
        h = hashlib.sha1()
        userAuth = user.username
        print('USER:'+userAuth+'|')
        h.update(userAuth.encode())
        print('HASH: '+h.hexdigest())
        if datad == h.hexdigest():
            message = user.username
        else:
            message = '404'    
    print('ENVIANDO: '+message)
        
    conn.sendall(message.encode()) 