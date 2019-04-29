import socket

# SERVER IP, PORT
IP = "10.3.51.103"
PORT = 8080

# String written by the user
msg = """AAACCGTTT\nlen\ncountA\ncountC"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((IP, PORT))

s.send(str.encode(msg))

response = s.recv(2048).decode()

# Printing the response from the server
print(response)
s.close()