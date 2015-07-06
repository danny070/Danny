__author__ = 'danny'

import socket

s = socket.socket()
#host = socket.gethostname()
#print(host)
port = 9999
s.bind(("", port))

s.listen(5)
while True:
    c, addr = s.accept()
    print ('Got connection from', addr)

    text = c.recv(1024)
    ss = text.decode('utf-8')
    c.send(ss.upper().encode('utf-8'))
    c.close()


