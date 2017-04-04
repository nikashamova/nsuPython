# coding=utf8
from argparse import ArgumentParser


class Table:
    u"""
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
        ideal = len(array[0])
        l = sum([1 for i in array if len(i) != ideal])
        if l != 0:
            raise FormatTableError
        self.array = array

    def head(self, count):
        if count < 0 or count > len(self.array):
            raise IndexError
        return Table([self.array[i] for i in range(count)])

    def tail(self, count):
        if count < 0 or count > len(self.array):
            raise IndexError
        return Table([self.array[i] for i in range(len(self.array) - count, len(self.array))])

    # row
    def get_row(self, index):
        if 0 > index or index >= len(self.array):
            raise TableIndexError
        return self.array[index]

    # column
    def get_column(self, index):
        if 0 > index or index >= len(self.array[0]):
            raise TableIndexError
        return [self.array[i][index] for i in range(len(self.array))]

    # concatenate
    def concatenate_by_rows(self, other):
        if len(self.array[0]) != len(other.array[0]):
            raise SizeError
        self.array = sum([self.array, other.array], [])

    # paste
    def concatenate_by_columns(self, other):
        if len(self.array) != len(other.array):
            raise SizeError
        j = 0
        for i in self.array:
            for k in other.array[j]:
                i.append(k)
            j += 1

    # cut
    def create_new_table_by_column_numbers(self, indexes):
        flag = sum([1 for i in indexes if (0 > i or i > len(self.array))])
        if flag != 0:
            raise TableIndexError
        new_res = [[self.array[k][j] for j in indexes] for k in range(len(self.array))]
        return Table(new_res)


class SizeError(Exception):
    pass


class TableIndexError(Exception):
    pass


class FormatTableError(Exception):
    pass


def config_parser():
    parser = ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    cut_parser = subparsers.add_parser('cut', help=u"выбрать определённые столбцы из таблицы")
    cut_parser.add_argument('-f', type=str)
    cut_parser.add_argument('name', type=open)

    head_parser = subparsers.add_parser('head', help=u"выбрать первые n строк из таблицы")
    head_parser.add_argument('-n', nargs=1, type=int)
    head_parser.add_argument('name', type=open)

    tail_parser = subparsers.add_parser('tail', help=u"выбрать последние n строк из таблицы")
    tail_parser.add_argument('-n', nargs=1, type=int)
    tail_parser.add_argument('name', type=open)

    paste_parser = subparsers.add_parser('paste', help=u"склеить две таблицы приписыванием столбцов")
    paste_parser.add_argument('name1', type=open)
    paste_parser.add_argument('name2', type=open)

    concatenate_parser = subparsers.add_parser('concatenate', help=u"склеить две таблицы приписыванием строк")
    concatenate_parser.add_argument('name1', type=open)
    concatenate_parser.add_argument('name2', type=open)

    row_parser = subparsers.add_parser('row', help=u"получить n-ую строку")
    row_parser.add_argument('name', type=open)
    row_parser.add_argument('-n', nargs=1, type=int)

    column_parser = subparsers.add_parser('column', help=u"получить n-ый столбец")
    column_parser.add_argument('name', type=open)
    column_parser.add_argument('-n', nargs=1, type=int)

    return parser


def run_command(namespace):
    if namespace.command == "cut":
        try:
            txt = namespace.name.read()
            indexes = [int(x) for x in namespace.f.split(",")]
            t = Table(convert_str_to_list(txt))
            print(t.array)
            res = t.create_new_table_by_column_numbers(indexes)
            print(res.array)
        except TableIndexError:
            print(u"не существует столбца с данным номером")
        except FormatTableError:
            print(u"неверный формат таблицы")
    elif namespace.command == "head":
        try:
            txt = namespace.name.read()
            t = Table(convert_str_to_list(txt))
            print(t.array)
            res = t.head(namespace.n[0])
            print(res.array)
        except IndexError:
            print(u"не существует такого количества строк")
        except FormatTableError:
            print(u"неверный формат таблицы")
    elif namespace.command == "tail":
        try:
            txt = namespace.name.read()
            t = Table(convert_str_to_list(txt))
            print(t.array)
            res = t.tail(namespace.n[0])
            print(res.array)
        except IndexError:
            print(u"не существует такого количества строк")
        except FormatTableError:
            print(u"неверный формат таблицы")
    elif namespace.command == "paste":
        try:
            txt = namespace.name1.read()
            t1 = Table(convert_str_to_list(txt))
            print(t1.array)

            txt = namespace.name2.read()
            t2 = Table(convert_str_to_list(txt))
            print(t2.array)

            t1.concatenate_by_columns(t2)
            print(t1.array)
        except SizeError:
            print(u"неправильное количество строк")
        except FormatTableError:
            print(u"неверный формат таблицы")
    elif namespace.command == "concatenate":
        try:
            txt = namespace.name1.read()
            t1 = Table(convert_str_to_list(txt))
            print(t1.array)

            txt = namespace.name2.read()
            t2 = Table(convert_str_to_list(txt))
            print(t2.array)

            t1.concatenate_by_rows(t2)
            print(t1.array)
        except SizeError:
            print(u"неправильное количество столбцов")
        except FormatTableError:
            print(u"неверный формат таблицы")
    elif namespace.command == "column":
        try:
            txt = namespace.name.read()
            t = Table(convert_str_to_list(txt))
            print(t.array)
            res = t.get_column(namespace.n[0])
            print(res)
        except TableIndexError:
            print(u"не существует столбца с данным номером")
        except FormatTableError:
            print(u"неверный формат таблицы")
    elif namespace.command == "row":
        try:
            txt = namespace.name.read()
            t = Table(convert_str_to_list(txt))
            print(t.array)
            res = t.get_row(namespace.n[0])
            print(res)
        except TableIndexError:
            print(u"не существует строки с данным номером")
        except FormatTableError:
            print(u"неверный формат таблицы")


def convert_str_to_list(s):
    return [[int(y) for y in x.split(',')] for x in s.split('\n')]


parser = config_parser()
a = parser.parse_args()
run_command(a)
