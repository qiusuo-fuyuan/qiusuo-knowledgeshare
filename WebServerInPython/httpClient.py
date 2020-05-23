#!/usr/bin/env python3

import socket
from datastructure import *

SERVER = "127.0.0.1"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

httpRequest = HttpProtocol(HttpMethod.GET,RequestURL.RNN_TRAIN,"training")
httpReuestString = serialize(httpRequest)

client.sendall(bytes(httpReuestString, 'UTF-8'))
while True:
    in_data = client.recv(1024)
    print("From Server :", in_data.decode())
    out_data = input()
    client.sendall(bytes(out_data, 'UTF-8'))
    if out_data == 'bye':
        break
client.close()
