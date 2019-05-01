import http.client
import json
import termcolor
from Seq import Seq

PORT = 8003
SERVER = 'http://rest.ensembl.org/'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method.

# As the FRAT1 gene is ENSG00000165879 in Ensemble, we write this request

conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

# -- Read the response message from the server

r1 = conn.getresponse()

# -- Print the status line

print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body

data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received

data = json.loads(data1)

# We see that our json has some parameters such as "desc", "query", "version", etc. The one we are going to use is "seq"

seq = data["seq"]

# Using the class Seq we already have

sequence = Seq(seq)

# Now we can answer the questions proposed in the practice

# 1-Bases of FRAT1
number1 = len(sequence)

# 2-T's in FRAT1
number2 = 0
for a in sequence:
    if a == "T":
        number2 = number2 + 1

# 3-Most popular base
number_a = 0
number_c = 0
number_g = 0
number_t = 0
for i in sequence:
    if i == "A":
        number_a = number_a + 1
    elif i == "C":
        number_c = number_c + 1
    elif i == "G":
        number_g = number_g + 1
    elif i == "T":
        number_t = number_t + 1
list_max = [number_a,number_c,number_g,number_t]
max_number = max(list_max, key=int)

# 4-Percentage most popular base


# 5-Percentage all bases




