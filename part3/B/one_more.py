import csv
from collections import Counter

file = open("input.txt", "r", encoding="utf-8")
count = int(file.readline())
prepared_words = ([w.lower().strip() for w in file.readlines()])

res = {}

for w in prepared_words:
    word_s = "".join(sorted(list(w)))
    if word_s in res:
        if w not in res[word_s]:
            res[word_s].append(w)
            res[word_s].sort()
    else:
        res[word_s] = [w]

ans = list(res.values())
total = [a for a in ans if len(a) > 1]
total.sort()

with open("output.txt", "w", encoding='utf-8', newline="", ) as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerows(total)
