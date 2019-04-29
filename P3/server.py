
from Seq import Seq
import socket

# IP, PORT
IP = "192.168.1.37"
PORT = 8080
MAX_OPEN_REQUEST = 5

list_resp = []

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

        if len(list_resp) == 0:
            sequence = Seq(list_msg[0])
            list_msg = list_msg[1:]
            list_resp.append("OK")
            for a in list_msg:
                if a == "len":
                    resp = sequence.len()
                elif a == "percA":
                    resp = sequence.perc("A")
                    list_resp.append(resp)
                elif a == "percC":
                    resp = sequence.perc("C")
                    list_resp.append(resp)
                elif a == "percG":
                    resp = sequence.perc("G")
                    list_resp.append(resp)
                elif a == "percT":
                    resp = sequence.perc("T")
                    list_resp.append(resp)
                elif a == "complement":
                    resp = sequence.complement()
                    list_resp.append(resp)
                elif a == "countA":
                    resp = sequence.count("A")
                    list_resp.append(resp)
                elif a == "countC":
                    resp = sequence.count("C")
                    list_resp.append(resp)
                elif a == "countT":
                    resp = sequence.count("T")
                    list_resp.append(resp)
                elif a == "countG":
                    resp = sequence.count("G")
                    list_resp.append(resp)
                elif a == "reverse":
                    resp = sequence.reverse()
                    list_resp.append(resp)
                else:
                    resp = "There was an error"
                    list_resp.append(resp)

        print(list_resp)
        list_answer = str(list_resp)
        msg_send = list_answer.replace(",", "\n").strip("[").strip("]")
        client3socket.send(str.encode(msg_send))

    client3socket.close()


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