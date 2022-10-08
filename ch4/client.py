import socket

s2 = socket.socket()
s2.connect(("127.0.0.1", 2345))
data = s2.recv(1024)
s2.close()
print("Received", repr(data))
print("Received", data.decode(encoding="utf-8"))
