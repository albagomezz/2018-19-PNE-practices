import socket
from P1.Seq import Seq

i = True
while i:
    seq = Seq(input('Introduce the sequence: '))
    comp = seq.complement()
    rev = seq.reverse()

    # Create a socket for communicating with the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Socket created')
    PORT = 8082
    IP = "10.3.50.22"

    # Connections needed:
    s.connect((IP, PORT))
    s.send(str.encode("The complement of the sequence is: {}".format(comp)))
    s.send(str.encode("\n"))
    s.send(str.encode("The reverse of the sequence is: {}".format(rev)))
    msg = s.recv(2048).decode("utf-8")
    print('MESSAGE FROM THE SERVER:')
    print(msg)

    s.close()
