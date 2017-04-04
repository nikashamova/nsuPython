import csv


def is_anagram(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))


file = open("input.txt", "r", encoding="utf-8")
count = int(file.readline())
prepared_words = ([w.lower().strip() for w in file.readlines()])

total = []
while len(prepared_words) != 0:
    word1 = prepared_words[0]
    checker = sorted(list(word1))
    result = [word1]
    del prepared_words[0]
    j = 0
    while j != (len(prepared_words)):
        word2 = prepared_words[j]
        if checker == sorted(list(word2)):
            result.append(word2)
            del prepared_words[j]
            j -= 1
        j += 1
    if len(result) > 1 and result not in total:
        total.append(sorted(result))

total.sort()
with open("output.txt", "w", encoding='utf-8', newline="", ) as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(total)


