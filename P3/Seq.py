
class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        l = len(self.strbases)
        return l

    def complement(self):
        bases_c = ""
        change = {"A": "T", "T": "A", "G": "C", "C": "G"}
        for i in self.strbases:
            bases_c += change[i]
        return bases_c

    def reverse(self):
        r = self.strbases[::-1]
        return Seq(r)

    def count(self, base):
        c = self.strbases.count(base)
        return c

    def perc(self, base):
        a = len(self.strbases)
        num = self.strbases.count(base)
        p=round(100.0*num/a, 1)
        return p


