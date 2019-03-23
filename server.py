import socket

host = '127.0.0.1'
port = 5000

s = socket.socket()
s.bind((host,port))
s.listen(1)

c,addr = s.accept()

while True:
    data = c.recv(1024)

    if not data:
        break
    print("Received" + str(data))
    data = str(data).upper()
    print("Sending" + data)
    c.send(data.encode())
c.close()