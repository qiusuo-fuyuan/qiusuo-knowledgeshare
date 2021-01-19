import time
from typing import List
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")

class Socket 
{
    clientIP: String
    clientPort: String
    serverIP: String
    serverPort: String
}

serverSocket("localhost", 9999)

newSocket = socket.accept()
newSocket1, newSocket2, newSocket3

class File {
    hasData: Boolean
}

List connectedClientSockets = [newSocket1, newSocket2, newSocket3]

content = newSocket1.recv()



newSocket2.recv()
















file1 = open("file1")
     file1.asyncio_read()
     fileArray.append(file1)

file2 = open("file2")
     file2.asyncio_read()
     fileArray.append(file2)

file3 = open("file3")
    file3.asyncio_read()
    fileArray.append(file3)


EventLoop Thread
while(true):
    foreach(file in fileArray):
        if(file.hasData):
            data = readData(file)




