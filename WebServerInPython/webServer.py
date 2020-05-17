import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)


class File {
    byte[] buffer,
    read():
    write()
}

class Socket {
    source:
    target:
    port: number
    interface: number
    byte[]: buffer
    read():
    write():
}


class Process {
    File[] files;
    Sockets[] sockets;
    Thread[] threads;
    currentExecuteCommand: 0xie24q30dsaesafdsu9;
}


class Processes {
    dict<port, Process> portToProcessMap;
}
lookUPProcessFromPort(input, output)