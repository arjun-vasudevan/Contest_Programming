from sys import stdin

N, L, R = map(int, stdin.readline().split())
solds   = sorted(map(int, stdin.readline().split()), reverse = True)
print sum(solds[i] for i in xrange(R - 1, N, L))
