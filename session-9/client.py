import socket

# SERVER IP, PORT
IP = "212.128.253.82"
PORT = 8080

# Create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

msg = "Hello"

# Close the socket
s.close()