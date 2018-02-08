#!/usr/bin/python3

import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', 1234))
mySocket.listen(5)

try:
    while True:
        print('Waiting for connections')
        (recvSocket, address) = mySocket.accept()
        print('Request received:')
        print(recvSocket.recv(2048))
        print('Answering back...')
        aleat = str(random.randrange(999999999))
        recvSocket.send(bytes(
                        "HTTP/1.1 200 OK\r\n\r\n" +
                        "<html><body><h1>Hola.</h1>" +
                        "<a href=" + aleat + ">Dame otra</a>" +
                        "</body></html>" +
                        "\r\n", "utf-8"))
        recvSocket.close()

except KeyboardInterrupt:
    print("Closing binded socket")
    mySocket.close()
