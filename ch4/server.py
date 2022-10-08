import socket

sl = socket.socket()
sl.bind(("127.0.0.1", 2345))
sl.listen(5)
while 1:
    conn, address = sl.accept()
    print("a new connect from", address)
    conn.sendall(bytes("Hello world", encoding="utf-8"))
    conn.close()
