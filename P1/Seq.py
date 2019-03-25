
class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        l = len(self.strbases)
        return l

    def complement(self):
        c = self.strbases
        for index, i in enumerate(c):
            if i == 'A':
                c = c[:index]+c[:index].replace('A', 'T')

            elif i == 'T':
                c = c[:index]+c[:index].replace('T', 'A')

            elif i == 'C':
                c = c[:index] + c[:index].replace('C', 'G')

            elif i == 'G:':
                c = c[:index] + c[:index].replace('G', 'C')
        return c

    def reverse(self):
        r = self.strbases[::-1]
        return Seq(r)

    def count(self, base):
        c = self.strbases.count(base)
        return c

    def perc(self, base):
        a = len(self.strbases)
        num = self.strbases.count(base)
        if a>0:
            p=round(100.0*num/a, 1)
            return p
        else:
            p=0
            return p

