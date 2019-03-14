from Seq import Seq

#this is going to be the main program of the practice 1

s1 = Seq(input("seq 1 is: "))
s2 = Seq(input("seq 2 is: "))

s3 = s1.complement()
s4 = s3.reverse()

sequences = [s1, s2, s3, s4]

for elem in sequences:
    