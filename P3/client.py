import socket

# SERVER IP, PORT
IP = "192.168.1.37"
PORT = 8080

# String written by the user
msg = """AAACCGTTT\nreverse\ncomplement\npercT"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((IP, PORT))

s.send(str.encode(msg))

response = s.recv(2048).decode()

# Printing the response from the server
print(response)
s.close()