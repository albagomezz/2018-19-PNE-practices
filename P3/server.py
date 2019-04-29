
from Seq import Seq
import socket

# IP, PORT
IP = "10.3.51.103"
PORT = 8080
MAX_OPEN_REQUEST = 5


def process_client(client3socket):
    # Reading the message from the client.
    msg = client3socket.recv(2048).decode("utf-8")
    list_msg = msg.split('\n')
    first = msg[0]

    if first == "":
        client3socket.send(str.encode("ALIVE"))
    else:
        for i in first:
            if i != "A" and i != "C" and i != "G" and i != "T" :
                not_valid = "Sequence not valid"
                client3socket.send(str.encode(not_valid))
                break
            else: continue

    elif :

        print(answer_list)
        answer_list = str(answer_list)
        msg_send = answer_list.replace(",", "\n").strip("[").strip("]")
        client3socket.send(str.encode(msg_send))

    client3socket.close()


# A partir de aqui esta hecho


# Create a socket for connecting to the clients
thirdsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

thirdsocket.bind((IP, PORT))
thirdsocket.listen(MAX_OPEN_REQUEST)

print("Socket ready at: {}".format(thirdsocket))

while True:
    print("Waiting for connections at: {}, {}".format(IP, PORT))
    (client3socket, address) = thirdsocket.accept()
    # Wait until client connects

    print("Attending connections from client: {}".format(address))
    process_client(client3socket)