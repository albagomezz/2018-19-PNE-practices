
class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def len(self):
        l = len(self.strbases)
        return l

    def complement(self):

    def reverse(self):
        r = self.strbases[::-1]
        return r

    def count(self, base):
        c = self.strbases.count(base)
        return c

    def perc(self, base):
        a = self.strbases.len(base)
        num = self.strbases.count(base)
        if a>0:
            p=round(100.0*num/a)
        else:
            p=0
            return p

