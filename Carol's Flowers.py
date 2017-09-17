from sys import stdin

F, N = map(int, stdin.readline().split())
flowers = sorted((int(stdin.readline()) for _ in xrange(F)))

flowers = flowers[:N][::-1]

cost = 0
for i in xrange(1, N + 1):
    cost += flowers[i - 1] ** i

print cost % (10 ** 9 + 7)
