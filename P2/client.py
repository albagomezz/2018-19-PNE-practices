#first we define the class

class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def complement(self):
        bases_c = ""
        change = {"A": "T", "T": "A", "G": "C", "C": "G"}
        for i in self.strbases:
            bases_c += change[i]
        return bases_c

    def reverse(self):
        r = self.strbases[::-1]
        return Seq(r)


#then we create our main program

import socket

connected = True
while connected:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")

    PORT = 8081
    IP = "212.128.253.105"

    s.connect((IP, PORT))

    s1 = Seq(input("Introduce the sequence to obtain the reverse-complement sequence: "))
    s2 = Seq(s1.reverse()).complement()
    print("The reverse-complement sequence is: ", s2)

    s.send(str.encode(s2))
    s.close()
    print("The sequence has been sent to the server")
