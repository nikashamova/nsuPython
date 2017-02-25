def count_letters(word, result):
    word = word.lower()
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if not letter in result:
            result[letter] = word.count(letter)
        else:
            c = word.count(letter)
            result[letter] += word.count(letter)
    return result


file_input = open("input.txt", "r")
file_output = open("output.txt", "w")

lines = file_input.readlines()
result = {}

for l in lines:
    result = (count_letters(l, result))

result = {k: v for k, v in result.items() if v}
sorted_list = [(k, -v) for v, k in sorted([(-v, k) for k, v in result.items()])]

for k, v in sorted_list:
    file_output.write(k + ": " + str(v) + "\n")

file_input.close()
file_output.close()
