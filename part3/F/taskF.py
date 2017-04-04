import argparse


def get_number(c):
    s = "@%#*+=-:. "
    for i in range(len(s)):
        if c == s[i]:
            return i
    return s[len(s) - 1]


def rotate_clockwise(matrix, degree=90):
    return matrix if not degree else rotate_clockwise(zip(*matrix[::-1]), degree - 90)


s = "@%#*+=-:. "

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

crop_parser = subparsers.add_parser('crop')
crop_parser.add_argument('-r', '--right', type=int)
crop_parser.add_argument('-l', '--left', type=int)
crop_parser.add_argument('-t', '--top', type=int)
crop_parser.add_argument('-b', '--bottom', type=int)

expose_parser = subparsers.add_parser('expose')
expose_parser.add_argument('num', type=int)

rotation_parser = subparsers.add_parser('rotate')
rotation_parser.add_argument('degree', type=int)

file = open("input.txt", "r")
output = open("output.txt", "w")

command = file.readline()
namespace = parser.parse_args(command.split())
pic = file.readlines()
pic = [x.replace("\n", "") for x in pic if x != "\n"]

if namespace.command == 'crop':
    if namespace.right is not None:
        pic = [row[:len(pic[0]) - namespace.right] + row[len(pic[0]):] for row in pic]
    if namespace.left is not None:
        pic = [row[:0] + row[namespace.left:] for row in pic]
    if namespace.top is not None:
        pic = pic[namespace.top:]
    if namespace.bottom is not None:
        pic = pic[0:len(pic) - namespace.bottom]

    for s in pic:
        output.write(s + "\n")
elif namespace.command == "expose":
    result = []
    for l in pic:
        tmp = []
        for x in l:
            number = get_number(x) + namespace.num
            if number > len(s) - 1:
                number = len(s) - 1
            tmp.append(s[number])
        result.append(''.join(tmp))
    pic = result
    for s in pic:
        output.write(s + "\n")
elif namespace.command == "rotate":

    if namespace.degree == 90:
        i = len(pic[0])
        while i > 0:
            i -= 1
            output.write(''.join(x[i] for x in pic) + "\n")
    elif namespace.degree == 180:
        i = len(pic)
        while i > 0:
            i -= 1
            output.write(''.join(reversed(list(pic[i]))) + "\n")
    elif namespace.degree == 270:
        i = 0
        while i < len(pic[0]):
            output.write(''.join(reversed([x[i] for x in pic])) + "\n")
            i += 1
