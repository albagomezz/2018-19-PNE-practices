import http.client
import json
import termcolor

PORT = 8003
SERVER = 'http://rest.ensembl.org/'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method.

# As the FRAT1 gene is ENSG00000165879 in Ensemble, we write this request

conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

