from Seq import Seq

#this is the main program of the practice 1

s1 = Seq("ACGTACGTA")
s2 = Seq("GGTGGTAC")

s3 = Seq(s1.complement())
s4 = Seq(s3.reverse())

sequences = [s1, s2, s3, s4]

for elem in sequences:
    print("Sequence: ", elem)
    print(" Length: ", elem.len())
    print(" Bases count: A: {}".format(elem.count('A')), "T: {}".format(elem.count('T')), "C: {}".format(elem.count('C')), "G: {}".format(elem.count('G')))
    print(" Bases percentage: A: {}%".format(elem.perc('A')), "T: {}%".format(elem.perc('T')), "C: {}%".format(elem.perc('C')), "G: {}%".format(elem.perc('G')))

