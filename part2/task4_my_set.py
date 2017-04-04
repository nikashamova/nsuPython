import itertools


class X:
    def __init__(self, set_):
        self.__my_set = set_
        self.__cur = set_[0]
        self.__num = 0

    def get_current(self):
        return self.__cur

    def get_next(self):
        self.__num = (self.__num + 1) % len(self.__my_set)
        self.__cur = self.__my_set[self.__num]
        return self.__cur

    def get_len(self):
        return len(self.__my_set)


def create_list(x_):
    start = x_.get_current()
    cur = x_.get_next()
    result = [start]
    while cur != start:
        result.append(cur)
        cur = x_.get_next()
    return result


def generate_descartes(x_, n):
    my_list = [create_list(x_)] * n
    for element in itertools.product(*my_list):
        print(element)


x = X([1, 'a'])
print(x.get_next())
print(x.get_next())
print(x.get_next())
print(x.get_next())
generate_descartes(x, 3)
