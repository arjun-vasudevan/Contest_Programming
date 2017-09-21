import sys

cards = {}
N, T = [int(x) for x in sys.stdin.readline()[:-1].split()]
combs = []

for i in range(N):
    name, cost = sys.stdin.readline().split()
    cards[name] = int(cost)

for i in cards.keys():
    for j in cards.keys():
        for k in cards.keys():
            if i != j and j != k and i != k:
                if cards[i] + cards[j] + cards[k] <= T:
                    names = [i, j, k]
                    names.sort()
                    if names not in combs:
                        combs.append(names)

combs.sort()
for i in combs:
    print " ".join(i)
