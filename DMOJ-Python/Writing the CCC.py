from sys import stdin

types = {stdin.readline(): i + 1 for i in xrange(int(stdin.readline()))}

probs = [(stdin.readline(), j + 1) for j in xrange(int(stdin.readline()))]
probs.sort(key = lambda x: types[x[0]])

for i in probs:
    print i[1]
