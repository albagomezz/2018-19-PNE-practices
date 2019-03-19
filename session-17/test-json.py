import json
import termcolor

f = open("person.json", 'r')

person = json.load(f)

print()

termcolor.cprint("Name: ", 'green', end='')
print(person['Firstname'], person['Lastname'])
termcolor.cprint("Age: ", 'red', end="")
print(person['Age'])

for i,num in enumerate(person["Phonenumber"]):
    termcolor.cprint("Phone {}: ".format(i), 'yellow', end='')
    # The element num contains 2 fields: number and type
    termcolor.cprint("    Type: ", 'blue', end='')
    print(num['type'])
    termcolor.cprint("    Number: ", 'blue', end='')
    print(num['number'])