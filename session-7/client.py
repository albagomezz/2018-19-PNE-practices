# programming our first client

import socket

# create a socket for communicating with the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Socket created")

PORT = 8080
IP = "212.128.253.64"

s.connect((IP, PORT))

s.send(str.encode("alba ruiz prestame el cable para el movil"))

msg = s.recv(2048).decode("utf-8")

print("MESSAGE FORM THE SERVER: ")




print(msg)

s.close()

print("The end")