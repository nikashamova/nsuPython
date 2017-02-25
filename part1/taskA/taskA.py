def fibonacci(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

file_input = open("input.txt", "r")
n = int(file_input.readline())
file_output = open("output.txt", "w")
file_output.write(str(fibonacci(n)))
file_input.close()
file_output.close()
