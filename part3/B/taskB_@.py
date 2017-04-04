import csv


def is_anagram(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))


file = open("input.txt", "r", encoding="utf-8")
count = int(file.readline())
prepared_words = (([w.lower().strip() for w in file.readlines()]))
total = []
added = []
for i in range((len(prepared_words))):
    if i in added:
        continue
    indexes = [i]
    word1 = prepared_words[i]
    result = [word1]
    for j in range(i + 1, len(prepared_words)):
        word2 = prepared_words[j]
        if is_anagram(word1, word2) and j not in added:
            added.append(j)
            indexes.append(j)
            result.append(word2)
            result = sorted(result)
    if len(result) > 1 and result not in total:
        total.append(result)
        added.append(i)

total.sort()
with open("output.txt", "w", encoding='utf-8', newline="", ) as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(total)
