import re
import collections


def get_all_combinations(list_, depth):
    result = []
    ans = []
    start = 0
    end = depth
    for j in range(len(list_) - depth + 1):
        tmp = []
        for k in range(start, end):
            tmp.append(list_[k])
        result.append(" ".join(tmp))
        start += 1
        end += 1
        ans.append([[tmp[i] for i in range(0, len(tmp) - 1)], [tmp[len(tmp) - 1]]])
    return ans


class Probe:
    def __init__(self, main_expression):
        self.expr = main_expression
        self.elements = []
        self.sample = []
        self.length = 0

    def add(self, sentence):
        # self.length += 1
        # if sentence not in set().union(*(d.keys() for d in self.elements)):
        #     self.elements.append({sentence: 1})
        # else:
        #     for e in self.elements:
        #         for key in e:
        #             if key == sentence:
        #                 e[sentence] += 1
        #                 return

        print(sentence)
        if sentence not in dict(self.sample):
            self.sample.append((sentence, 1))
        else:
            for s in self.sample:
                if s[0] == sentence:
                    s_ = (s[0], s[1] + 1)
                    self.sample.remove(s)
                    self.sample.append(s_)
                    return

    def get_probes(self):
        print(self.sample)
        print(sorted(self.sample))
        print(self.elements)
        return [(key, x[key] / self.length) for x in self.sample for key in x]
        # return [{key: x[key] / self.length} for x in self.elements for key in x]


class Generator:
    def __init__(self, text='', depth=1):
        self._text = text
        self._depth = depth
        self._tokens = {}
        self._punctuation = []
        self._no_punct_txt = ""
        self._probes = []

    def tokenize_text(self):
        token_pattern = re.compile("(([a-zA-Z])+)|(\d+)")
        punctuation_pattern = re.compile("([^\w\s])")

        result = re.finditer(token_pattern, txt)
        self._tokens = [r.group() for r in result]
        self._no_punct_txt = " ".join(self._tokens)
        self._tokens = set(self._tokens)
        result = re.finditer(punctuation_pattern, txt)
        self._punctuation = [r.group() for r in result]

    def probs(self):
        for d in range(1, self._depth + 1):
            words = self._no_punct_txt.split()
            comb = get_all_combinations(words, d)
            total = {}
            for c in comb:
                key = " ".join(c[0])
                if key not in total:
                    total[key] = c[1]
                else:
                    total[key] += c[1]

            ans = []
            for t in total:
                key = t
                sentence = total[key]
                probe = Probe(key)
                for s in sentence:
                    probe.add(s)
                ans.append(probe)

            self._probes.append(ans)

    def print_all_probes(self):
        for ans in self._probes:
            for a in ans:
                print(str(a.expr))
                list_ = a.get_probes()
                for map_ in list_:
                    for m in map_:
                        print(" " + m + ": " + "{0:.2f}".format(map_[m]))

    def print_all_probes_tuple(self):
        print(self._probes)
        for ans in self._probes:
            print(" " + ans.expr)
            for el in ans.sample:
                print(el)


tmp = []
tmp.append(("lol", 1))
tmp.append(("kek", 3))
tmp.append(("aaa", 5))
if "aaa" not in dict(tmp):
    tmp.append(("heh", -1))
print(sorted(tmp))
print(dict(tmp)["kek"])

txt = "First test sentence Second test line"  # 123! , lol .kek,!234 sk kek"
print(txt)
g = Generator(txt, 2)
g.tokenize_text()
g.probs()
g.print_all_probes_tuple()
# g.print_all_probes()
g.print_all_probes_tuple()
