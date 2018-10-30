import socket

c = socket.socket()
c.connect(('127.0.0.1',10000))

c.send(b'the god is a girl')
c.close()