import socket

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.connect(("127.0.0.1", 9999))

massage = s.recv(1024)

s.close()

print(massage.decode('ascii'))
