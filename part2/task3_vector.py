import math


class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __add__(self, other):
        return Vector([sum(x) for x in zip(self.vector, other.vector)])

    def __sub__(self, other):
        return Vector([i - j for i, j in zip(self.vector, other.vector)])

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector([i * other for i in self.vector])
        elif isinstance(other, self.__class__):
            return sum([i * j for i, j in zip(self.vector, other.vector)])

    def __eq__(self, other):
        return self.vector == other.vector

    def norma(self):
        return math.sqrt(sum([i * i for i in self.vector]))

    def get_by_index(self, index):
        return self.vector[index]

    def get_str(self):
        return str(self.vector)


v = Vector([9, 2, 3])
f = Vector([1, 1, 1])

print("V: " + v.get_str())
print("F: " + f.get_str())

print("SUM " + (v + f).get_str())
print("SUB " + (v - f).get_str())

print("CONSTANT MUL " + (v * 2).get_str())
print("SCALAR MUL " + str(v * f))

v1 = Vector([9, 2, 3])
print(v == v)
print(v == v1)
print(v == f)

f = Vector([3, -12, 2, 4, 5])
print(f.norma())
print(f.get_by_index(1))
print(f.get_str())
