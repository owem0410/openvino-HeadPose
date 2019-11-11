import socket
import datetime
import time
import sys
import os
from time import ctime

if __name__ == '__main__':	

    HOST = '127.0.0.1'
    PORT = 55555
    ADDRESS = (HOST, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
    server.bind((HOST, PORT))
    server.listen(5)    
    print(server.getsockname())
    print(u'waiting for connect...')
    connect, (host, port) = server.accept()
    peer_name = connect.getpeername()
    sock_name = connect.getsockname()
    print(u'the client %s:%s has connected.' % (host, port))
    print('The peer name is %s and sock name is %s' % (peer_name, sock_name))
    while 1:
        connect.sendall(b'angle')
        data = connect.recv(1024)
        print(b'the client say:' + data)
    server.close()
    
