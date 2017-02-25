def correct_bracket_sequence_identifier(line):
    stack = []
    for x in line:
        if x == "(" or x == "[" or x == "{":
            stack.append(x)
        elif x == ")":
            if not stack:
                return "no"
            tmp = stack.pop()
            if tmp != "(":
                return "no"
        elif x == "]":
            if not stack:
                return "no"
            tmp = stack.pop()
            if tmp != "[":
                return "no"
        elif x == "}":
            if not stack:
                return "no"
            tmp = stack.pop()
            if tmp != "{":
                return "no"
    if not stack:
        return "yes"
    return "no"


file_input = open("input.txt", "r")
file_output = open("output.txt", "w")

num = int(file_input.readline())
result = 0
for _ in range(num):
    line = file_input.readline()
    a = correct_bracket_sequence_identifier(line)
    file_output.write(a + "\n")

# file_output.write()


file_input.close()
file_output.close()
