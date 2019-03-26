# Getting information about the weather of
# a location introduced by the user

import http.client
import json

capital = input("Introduce the name of a capital to print weather info: ")

# -- API information
HOSTNAME = "www.metaweather.com"
ENDPOINT = "/api/location/search/?query={}".format(capital)
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPConnection(HOSTNAME)  #important check if here we have HTTPConnection or HTTPSConnection. If it doesnt work, try the other

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
number = json.loads(text_json)

# -- Print the received URL
print("The total number of jokes is:", number['woeid'])