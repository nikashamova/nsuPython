import csv


def is_anagram(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))


file = open("input.txt", "r", encoding="utf-8")
count = int(file.readline())
prepared_words = ([w.lower().strip() for w in file.readlines()])
total = []
answer = []
for i in range(len(prepared_words)):
    word = sorted(prepared_words[i])
    indexes = [i for i in range(len(prepared_words)) if sorted(prepared_words[i]) == word]
    if len(indexes) != 0 and indexes not in total:
        result = sorted([prepared_words[i] for i in indexes])
        total.append(indexes)
        answer.append(result)

answer.sort()
with open("output.txt", "w", encoding='utf-8', newline="", ) as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(answer)
