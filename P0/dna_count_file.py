a = c = t = g = 0
for line in open("dna.txt", "r"):
    line = line.replace("\n", "")
    for letter in line:
        if letter == 'A':
            a = a + 1
        elif letter == 'C':
            c = c + 1
        elif letter == 'T':
            t = t + 1
        elif letter == 'G':
            g = g + 1
        else:
            print("The sequence must contain only A,C,T and G")
            break
l = a + c + t + g
print("Total length: ", l)
print("A: ", a)
print("C: ", c)
print("T: ", t)
print("G: ", g)