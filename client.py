__author__ = 'danny'

import socket

s = socket.socket();
host = "localhost"
port = 9999

s.connect((host, port))

TEXT = input("Enter text: ")
s.send(TEXT.encode('utf-8'))

x = s.recv(1024).decode('utf-8')

print (x)

s.close()
