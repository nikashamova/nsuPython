import csv


def is_anagram(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))


file = open("input.txt", "r", encoding="utf-8")
count = int(file.readline())
prepared_words = ([w.lower().strip() for w in file.readlines()])
total = []
i = 0
while len(prepared_words) != 0:
    word = sorted(prepared_words[i])
    indexes_ = [i for i in range(len(prepared_words)) if sorted(prepared_words[i]) == word]
    indexes = sorted([prepared_words[i] for i in range(len(prepared_words))
                      if sorted(prepared_words[i]) == word])
    if len(indexes) != 0 and indexes not in total:
        total.append(indexes)
        off = 0
        for k in indexes_:
            prepared_words.pop(k - off)
            off += 1
    else:
        prepared_words.pop(i)

with open("output.txt", "w", encoding='utf-8', newline="", ) as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(total)
