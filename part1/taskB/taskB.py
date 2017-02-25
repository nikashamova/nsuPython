def part_creator(file_input, file_output):
    num = int(file_input.readline())
    for _ in range(num):
        line = file_input.readline()
        line = line.replace("\n", "")
        res = get_all_substrings(line)
        for r in res:
            file_output.write(r + " ")
        file_output.write("\n")


def get_all_substrings(s):
    length = len(s)
    res = [s[i:j] for i in range(length) for j in range(i + 1, length + 1)]
    res.sort(key=lambda item: (len(item)))
    return res

file_input = open("input.txt", "r")
file_output = open("output.txt", "w")
part_creator(file_input, file_output)
file_input.close()
file_output.close()
