class MySet:
    def __init__(self, my_set, count=1):
        self.my_set = my_set
        self.combinations = self.get_all_combinations(count)
        self.current = self.combinations[0]
        self.cur_num = 0

    def get_all_combinations(self, count):
        set_ = [(i, j) for i in self.my_set for j in self.my_set]
        self.combinations = set_
        return set_

    def get(self):
        return self.current

    def next(self):
        self.cur_num = (self.cur_num + 1) % len(self.combinations)
        self.current = self.combinations[self.cur_num]


s = [1, "a"]
m = {1, 2, 3}
s_ = MySet(s)
print(s_.combinations)
print(s_.get())
s_.next()
print(s_.get())
s_.next()
s_.next()
s_.next()
print(s_.get())
