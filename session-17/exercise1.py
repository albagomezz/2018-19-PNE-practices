import json
import termcolor

f = open("people.json", 'r')

people = json.load(f)

total = len(people["People"])
print("Total people in the data base: {}".format(total))

for num in people["People"]:
    termcolor.cprint("Name: ", 'green', end='')
    print(num['Firstname'], num['Lastname'])
    termcolor.cprint("Age: ", 'red', end="")
    print(num['Age'])


    for i, a in enumerate(num["Phonenumber"]):
        termcolor.cprint("Phone {}: ".format(i), 'yellow')
        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'blue', end='')
        print(a['type'])
        termcolor.cprint("    Number: ", 'blue', end='')
        print(a['number'])

