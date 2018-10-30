import socket

# 服务
s = socket.socket()     # 01创建一个套接字对象
print(s)

s.bind(('127.0.0.1',10000))     # 02绑定，此时是一个客户端
print(s)

# 5表示只有5个连接可以排队
s.listen(5)              # 03监听，监听后变成一个服务端

# 阻塞——没有客户端连接，保持等待状态
conn,addr = s.accept()              # 04对等套接字套接字；返回conn，addr地址、端口

# 05接受数据
conn.recv(1024)         # 表示可以接受1024个字符

# 06发送数据
conn.send(b'the god is a girl')     # 发送数据必须为byte类型

# 07断开连接
'''一般客户端主动关闭'''
'''client.close()'''