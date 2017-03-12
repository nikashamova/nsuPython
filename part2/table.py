class Table:
    def __init__(self, array):
        self.array = array

    def head(self):
        pass

    def tail(self):
        pass

    def get_row(self, index):
        return self.array[index]

    def get_column(self, index):
        return [self.array[i][index] for i in range(len(self.array))]

    def concatenate_by_rows(self, other_array):
        self.array = sum([self.array, other_array], [])

    def concatenate_by_columns(self, other_array):
        j = 0
        for i in self.array:
            for k in other_array[j]:
                i.append(k)
            j += 1

    def create_new_table_by_column_numbers(self, indexes):
        res = []
        for i in indexes:
            res.append(self.get_column(i))
        return res


my_table = Table([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
other = [[0, 0, 0], [1, 1, 1], [2, 2, 2]]
print(my_table.array[1])
print(my_table.get_row(2))
print(my_table.get_column(1))
my_table.concatenate_by_rows(other)
print(my_table.array)
print(my_table.create_new_table_by_column_numbers([0, 2]))
