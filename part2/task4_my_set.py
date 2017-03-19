class X:
    def __init__(self, set_, n):
        self.my_set = set_
        self.n = n
        self.capability = (len(self.my_set) ** n)

