class frac:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def mult(self, other):
        return frac(self.a*other.a, self.b*other.b)


