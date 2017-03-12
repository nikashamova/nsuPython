import math


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def add(self, other_vector):
        return [sum(x) for x in zip(self.vector, other_vector)]

    def subtract(self, other_vector):
        return [i - j for i, j in zip(self.vector, other_vector)]

    def constant_mult(self, alpha):
        return [i * alpha for i in self.vector]

    def scalar_mult(self, other_vector):
        return [i * j for i, j in zip(self.vector, other_vector)]

    def is_identical(self, other_vector):
        return self.vector == other_vector

    def norma(self):
        return math.sqrt(sum([i * i for i in self.vector]))

    def get_by_index(self, index):
        return self.vector[index]

    def get_str(self):
        return str(self.vector)


v = Vector([9, 2, 3])
print(v.subtract([4, 5, 6]))
print(v.scalar_mult([4, 5, 6]))
print(v.constant_mult(2))
print(v.is_identical([9, 2, 3]))
f = Vector([3, -12, 2, 4, 5])
print(f.norma())
print(f.get_by_index(1))
