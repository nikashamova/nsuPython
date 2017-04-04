import re

# pattern1 = re.compile('[0-9][0-9](\.|-|\/)[0-9][0-9](\.|-|\/)[0-9][0-9][0-9][0-9][^0-9]')
pattern10 = re.compile('[0-9][0-9](\.)[0-9][0-9](\.)[0-9][0-9][0-9][0-9][^0-9]')
pattern11 = re.compile('[0-9][0-9](-)[0-9][0-9](-)[0-9][0-9][0-9][0-9][^0-9]')
pattern12 = re.compile('[0-9][0-9](\/)[0-9][0-9](\/)[0-9][0-9][0-9][0-9][^0-9]')
# pattern2 = re.compile('[0-9][0-9][0-9][0-9](\.|-|\/)[0-9][0-9](\.|-|\/)[0-9][0-9][^0-9]')
pattern20 = re.compile('[0-9][0-9][0-9][0-9](\.)[0-9][0-9](\.)[0-9][0-9][^0-9]')
pattern21 = re.compile('[0-9][0-9][0-9][0-9](-)[0-9][0-9](-)[0-9][0-9][^0-9]')
pattern22 = re.compile('[0-9][0-9][0-9][0-9](\/)[0-9][0-9](\/)[0-9][0-9][^0-9]')
pattern3 = re.compile(u'[0-9]?[0-9]( )*[а-я]+( )*[0-9][0-9][0-9][0-9]', re.U)
file = open("input.txt", "r", encoding="utf-8")
output = open("output.txt", "w")
for line in file.readlines():
    if re.match(pattern10, line) or re.match(pattern11, line) or re.match(pattern12, line) \
            or re.match(pattern20, line) \
            or re.match(pattern21, line) or re.match(pattern22, line) or re.match(pattern3, line):
        output.write("YES" + "\n")
    else:
        output.write("NO" + "\n")
