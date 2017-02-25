def create_new_line(line, num):
    result = ""
    cur_sum = 0
    for word in line.split():
        word_len = len(word)
        if cur_sum + word_len <= num:
            cur_sum += word_len + 1
        else:
            cur_sum = 0
            result += "\n"
        result += word + " "
    result = result[:-1]
    return result


file_input = open("input.txt", "r")
file_output = open("output.txt", "w")

num = int(file_input.readline())
lines = file_input.readlines()

for line in lines:
    file_output.write(create_new_line(line, num) + "\n")


file_input.close()
file_output.close()
