# coding=utf8
from argparse import ArgumentParser


class Table:
    """
    Класс таблицы, который хранит данные в виде двумерной таблицы.

    ...

    Attributes
    ----------
    array: list[list]
        Список списков, представляющий собой двумерную таблицу.

    Methods
    -------
    head(count)
        Возвращает первые count строк.
    tail(count)
        Возвращает последние count строк.
    get_row(index)
        Возвращает строку с номером index.
    get_column(index)
        Возвращает столбец с номером index.
    concatenate_by_rows(other_array):
        Возвращает таблицу, полученную путём слияние искомой таблицы с other_array приписыванием строк other_array.
    concatenate_by_columns(other_array):
        Возвращает таблицу, полученную путём слияние искомой таблицы с other_array приписыванием столбцоы other_array.
    create_new_table_by_column_numbers(indexes):
        Возврашает новую таблицу, полученную из столбцов с номерами из indexes.

    """

    def __init__(self, array):
        self.array = array

    def head(self, count):
        return [self.array[i] for i in range(count)]

    def tail(self, count):
        return [self.array[i] for i in range(len(self.array) - count, len(self.array))]

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
        new_res = [[self.array[k][j] for j in indexes] for k in range(len(self.array))]
        return Table(new_res)


parser = ArgumentParser("HELLO")
# parser.add_argument('cut')

parser.add_argument('option', nargs=8, help='Выберите, что вы хотите сделать с таблицей')

subparsers = parser.add_subparsers(help="command")

number_parser = subparsers.add_parser('count', help="numbers")
name_parser = subparsers.add_parser('name', nargs=1, help="file name")

a = parser.parse_args()
if a.option == "cut":
    print("hello")
else:
    print("not hello")

# my_table = Table([
#     [1, 2, 3],
#     [0, 4, 5],
#     [6, 7, 8]])
# other = [
#     [0, 0, 0],
#     [1, 1, 1],
#     [2, 2, 2]]
#
# print(my_table.head(2))
# print(my_table.tail(2))
#
# print(my_table.get_row(2))
# print(my_table.get_column(1))
#
# # my_table.concatenate_by_rows(other)
# my_table.concatenate_by_columns(other)
# print(my_table.array)
#
# new_table = my_table.create_new_table_by_column_numbers([0, 2])
# print(new_table.array)
