from sys import stdin

N, Q = map(int, stdin.readline().split())
epi  = map(int, stdin.readline().split())

a = [0]
for i in epi:
    a.append(a[-1] + i)
total = a[-1]

for i in xrange(Q):
    start, stop = map(int, stdin.readline().split())
    print total - a[stop] + a[start - 1])
