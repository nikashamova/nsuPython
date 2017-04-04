output = open("output.txt", "w", encoding="utf-8")
languages = {}
result = {}
answer = set()
with open("input.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    while line != "\n":
        (key, val) = line.split()
        languages[key] = val
        result[key] = 3
        line = file.readline()
    total = set()
    for line in file:
        query = line.split(" ")
        total.clear()
        for q in query:
            result = {x: 0 for x in result}
            for c in q:
                for l in languages:
                    if c.lower() in languages[l]:
                        result[l] += 1
            max = 0
            for r in result:
                if result[r] > max:
                    max = result[r]
                    answer.clear()
                    answer.add(r)
                elif result[r] == max and max != 0:
                    answer.add(r)
            if len(list(answer)) != 0:
                answer_ = sorted(list(answer))[0]
                answer.clear()
                total.add(answer_)
        output.write(" ".join(sorted(list(total))) + "\n")
