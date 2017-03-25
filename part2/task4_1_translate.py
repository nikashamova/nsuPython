# coding=utf8
from argparse import ArgumentParser
import argparse
from sys import stdin
from sys import stdout


def change_symbols(old_symbols, new_symbols, s):
    res = s
    for i in range(len(old_symbols)):
        res = res.replace(old_symbols[i], new_symbols[i])
    return res


def delete_symbols(symbols, s):
    res = s
    for i in range(len(symbols)):
        res = res.replace(symbols[i], '')
    return res


def config_parser():
    parser = ArgumentParser()
    parser.add_argument('current', type=str)
    parser.add_argument('new', type=str)
    parser.add_argument('-d', '--delete', type=str)
    parser.add_argument('-i', '--input', type=open)
    parser.add_argument('-o', '--output', type=argparse.FileType('w'))
    return parser


class WrongLenException(Exception):
    pass


class CycleException(Exception):
    pass


def translate(namespace):
    if any(c in namespace.new for c in namespace.current):
        raise CycleException
    if len(namespace.current) != len(namespace.new):
        raise WrongLenException
    if namespace.input is not None:
        f = namespace.input
    else:
        f = stdin
    if namespace.output is not None:
        out = namespace.output
    else:
        out = stdout
    for line in f:
        result = line
        if namespace.delete is not None:
            result = delete_symbols(namespace.delete, line)
        result = change_symbols(namespace.current, namespace.new, result)
        out.write(result)


p = config_parser()
namespace = p.parse_args()
try:
    translate(namespace)
except WrongLenException:
    print("Длины строк не совпадают")
except CycleException:
    print("Обнаружен цикл замены")
