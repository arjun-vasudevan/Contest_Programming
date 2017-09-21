from sys import stdin

N, M = [int(_) for _ in stdin.readline()[:-1].split()]
docs = []

for i in range(M):
    own, shared = [int(_) for _ in stdin.readline()[:-1].split()]
    title = stdin.readline()[:-1]
    docs.append([shared, title])

mine = int(stdin.readline())

for i in docs:
    if i[0] == mine:
        print i[1]
