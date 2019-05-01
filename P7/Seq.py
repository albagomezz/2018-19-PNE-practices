
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
        for i in self:
            if i == "A":
                number_a = number_a + 1
            elif i == "C":
                number_c = number_c + 1
            elif i == "G":
                number_g = number_g + 1
            elif i == "T":
                number_t = number_t + 1
        c = {"A": number_a, "C": number_c, "G": number_g,"T": number_t}
        return c

    def perc(self, base):
        a = len(self.strbases)
        num = self.strbases.count(base)
        p=round(100.0*num/a, 1)
        return p


