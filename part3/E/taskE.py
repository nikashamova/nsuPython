import re

file = open("input.txt", "r")
output = open("output.txt", "w")

pattern0 = re.compile("import +")
pattern1 = re.compile("(\s)*import(\s)+")
pattern2 = re.compile(".*from.*import")

ans = []
for line in file.readlines():
    result = [x.strip().replace(";", "") for x in (re.split(pattern0, line))
              if x != "\n" and x != '' and x is not None]
    res_import = re.finditer(pattern1, line)
    res_import1 = re.match(pattern1, line)
    if result is not None and res_import1 is not None:
        for r in result:
            if r != "" and r != "\n":
                tmp = r.split(', ')
                for t in tmp:
                    ans.append(t)
    res_from = re.match(pattern2, line)
    if res_from is not None:
        ans.append(line[res_from.end() - 9: res_from.end() - 7])
ans = list(set(ans))
ans.sort()
for i in range(len(ans) - 1):
    output.write(ans[i] + ", ")
output.write(ans[len(ans) - 1])
