import socket
from P1.Seq import Seq

PORT = 8080
IP = "10.3.50.22"
MAX_OPEN_REQUEST = 5

def process_client(cs):
    #reading the message from the client
    msg = cs.recv(2048).decode("utf-8")

    print("Message from the client: {}".format(msg))
    #sending the message back to the client (bc we are an echo server)
    cs.send(str.encode(msg))

# Create a socket for connecting to the clients
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((IP, PORT))

serversocket.listen(MAX_OPEN_REQUEST)

print("Socket ready: {}".format(serversocket))

while True:
    print("Waiting for connections at {}, {} ".format(IP, PORT))
    (clientsocket, address) = serversocket.accept()

    # Connection received. A new socket is returned for communicating with the client
    print("Attending connections from client: {}".format(address))

    # This server do nothing. The new socket is closed
    clientsocket.close()
