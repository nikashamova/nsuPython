import re

file = open("input.txt", "r", encoding="utf-8")
output = open("output.txt", "w", encoding="utf-8")
count = int(file.readline())
regex = re.compile('[^а-я]')
for i in range(count):
    s = file.readline()
    s = s.lower()
    s = s.replace('ё', 'е')
    s = regex.sub('', s)
    #print(s)
    if s == s[::-1]:
        output.write('yes\n')
    else:
        output.write('no\n')


