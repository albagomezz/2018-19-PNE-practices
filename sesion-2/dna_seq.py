dna = str(input("Introduce the sequence: "))
dna = dna.upper()

a=c=t=g=0
for letter in dna:
    if letter == 'A':
        a=a+1
    elif letter == 'C':
        c=c+1
    elif letter == 'T':
        t=t+1
    elif letter == 'G':
        g=g+1
    else:
        print("The sequence must contain only A,C,T and G")
        break

l = len(dna)
print("Total length: ", l)
print("A: ",a)
print("C: ",c)
print("T: ",t)
print("G: ",g)
