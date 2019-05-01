import http.client
import json
import termcolor

PORT = 8003
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
people = json.loads(data1)

print("CONTENT: ")

# Print the information in the object
total = len(people["People"])
print("Total people in the data base: {}".format(total))

for num in people["People"]:
    termcolor.cprint("Name: ", 'green', end='')
    print(num['Firstname'], num['Lastname'])
    termcolor.cprint("Age: ", 'red', end="")
    print(num['Age'])
# Get the phoneNumber list
    phoneNumbers = num['Phonenumber']

# Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'yellow', end='')
    print(len(phoneNumbers))

# Print all the numbers
    for i, a in enumerate(phoneNumbers):
        termcolor.cprint("Phone {}: ".format(i), 'magenta')
        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'blue', end='')
        print(a['type'])
        termcolor.cprint("    Number: ", 'blue', end='')
        print(a['number'])