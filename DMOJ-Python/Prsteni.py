from sys import stdin
from fractions import gcd

N = int(stdin.readline())
rings = map(int, stdin.readline().split())

for i in rings[1:]:
    g = gcd(rings[0], i)

    print str(rings[0] / g) + '/' + str(i / g)
