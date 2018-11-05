#!/usr/bin/env python

import socket
import recognition

TCP_IP = '127.0.0.1'
TCP_PORT = 8080
BUFFER_SIZE = 1024  # Tamanho padrao

# Criacao do socket para conexao
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket criado com sucesso")

# Associação da aplicacao com a porta especificada
s.bind((TCP_IP, TCP_PORT))
print ("Associacao feita com sucesso")

# Escuta iniciada para novas conexoes
s.listen(1)
print ("Escutando na porta ", TCP_PORT)

# Aprovacao da conexao
conn, addr = s.accept()
print ('Endereço da conexão:', addr)

# A unica conexao fica aberta por tempo indefinido (ou ate o aparelho ser desligado)
while 1:
    
    # Recebe o dado do arduino
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print ("Dado recebido:", data)

    # Executa identificacao de conteudo
    ans = recognition.recognize(data)

    # Responde se o aparelho deve ou nao desligar
    if ans:
        conn.send(False)
    else:
        conn.send(True)

# Fecha conexao
conn.close()