#!/usr/bin/env python

import socket
import recognition as rc


TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024  # Tamanho padrao

# Criacao do socket para conexao
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associação da aplicacao com a porta especificada
s.bind((TCP_IP, TCP_PORT))

# Escuta iniciada para novas conexoes
s.listen(1)

# Aprovacao da conexao
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print "received data:", data
    ans = rc.rcognize(data)
    if (ans):
        conn.send(false)  # Envia sinal de resposta
    else:
        conn.send(true)
# Fecha conexao
conn.close()