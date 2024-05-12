import socket

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9999))

s.listen()

print("Listening...")

while True:

    client, address = s.accept()
    print("connected to {}".format(address))
    massage = "Hello Welcome To My Site !"
    client.send(massage.encode('ascii'))
    client.close()
