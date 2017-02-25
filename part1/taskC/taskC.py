def p_norm_calculator(p, vect):
    return sum([v ** p for v in vect]) ** (1 / p)


file_input = open("input.txt", "r")
file_output = open("output.txt", "w")

p = int(file_input.readline())
input_str = file_input.readline().split()
vect = [float(x) for x in input_str]

result = p_norm_calculator(p, vect)
file_output.write(str(result))

file_input.close()
file_output.close()
