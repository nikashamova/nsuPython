with open('input.txt') as file:
    n = int(file.readline())

    rest = n
    current = ""
    need_space = True

    for line in file:
        for word in line:
            if word in (' ', '\n'):
                if current == '':
                    print('', end='')
                elif len(current) >= n:
                    if rest != n:
                        print()
                    print(current)
                    rest = n
                elif rest == n:
                    print(current, end='')
                    rest -= len(current)
                elif len(current) + 1 <= rest:
                    print(' ', current, end='')
                    rest -= len(current) + 1
                else:
                    print()
                    print(current, end='')
                    rest = n - len(current)
                current = ''
                if word == '\n':
                    print()
                    rest = n
            else:
                current += word
