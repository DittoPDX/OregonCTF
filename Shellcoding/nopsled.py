import socket

host = "54.89.227.20"
port = 37008

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

nop = '\x90' * 8

s.send(nop)
s.send("^")
print s.recv(100)
s.close()
