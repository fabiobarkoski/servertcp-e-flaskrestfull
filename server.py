import socket
from models import Users, Product
import hashlib
import json

# IP e porta do servidor
HOST = '127.0.0.1'
PORT = 80

# criando o socket do server TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Server Rodando!')
s.bind((HOST, PORT))
# esperando conexao de cliente
s.listen()
conn, addr = s.accept()
print('Conectado por: ', addr)
# loopíng de receber dados, checar,
# consultar banco de dados e enviar informações
while True:
    data = conn.recv(1024)
    if not data:
        break
# decodificação dos dados JSON recebidos
    datad = data.decode()
# conversão de JSON para python
    dataJson = json.loads(datad)
    print(f'{dataJson} enviado de:  + {addr}')
    message = None
# inicio da checagem de usuario que está realizando consulta
    userAll = Users.query.all()
    for user in userAll:
        h = hashlib.sha1()
        userAuth = user.password
        print('PASSWORD:'+userAuth)
        h.update(userAuth.encode())
        print('COMPARANDO {} COM {}'.format(dataJson['hash'], h.hexdigest()))
        hcomp = h.hexdigest()
# comparando hash do banco de dados com a recebida pela API
        if dataJson['hash'] == hcomp:
            print('VERIFICA')
# inicio das consultas do servidor ao banco de dados e retorno para API
            if dataJson['to'] == 'products':
                if dataJson['method'] == 'GET':
                    product = Product.query.all()
                    message = json.dumps(
                        [{'id': p.id,
                          'name': p.name,
                          'type': p.type,
                          'amount': p.amount} for p in product])
                    break

                elif dataJson['method'] == 'POST':
                    product = Product(name=dataJson['name'],
                                      type=dataJson['type'],
                                      amount=dataJson['amount'])
                    product.commit()
                    message = json.dumps({'status': 200,
                                          'message': 'Produto cadastrado!'})
                    break

                elif dataJson['method'] == 'PUT':
                    product = Product.query.filter_by(
                        id=dataJson['id']).first()
                    product.name = dataJson['name']
                    product.type = dataJson['type']
                    product.amount = dataJson['amount']
                    product.commit()
                    message = json.dumps({'status': 200,
                                          'message': 'Produto alterado!'})
                    break

                elif dataJson['method'] == 'DELETE':
                    product = Product.query.filter_by(
                        id=dataJson['id']).first()
                    product.delete()
                    message = json.dumps({'status': 200,
                                          'message': 'Produto deletado!'})
                    break
            else:
                if dataJson['method'] == 'GET':
                    message = json.dumps({'name': user.username,
                                          'password': user.password,
                                          'Authenticator': dataJson['hash']})
                    break

                elif dataJson['method'] == 'PUT':
                    user.password = dataJson['password']
                    message = json.dumps({'status': 200,
                                          'message': 'Senha alterada!'})
                    break
        else:
            message = json.dumps({'status': 404,
                                  'message': 'Hash de usuário incorreta'})

    print('ENVIANDO: '+message)
    conn.sendall(message.encode())
