from sys import stdin

davScore, antScore = 100, 100

for _ in xrange(int(stdin.readline())):
    ant, dav = map(int, stdin.readline().rstrip('\n').split())

    if ant > dav:
        davScore -= ant
    elif ant < dav:
        antScore -= dav

print antScore
print davScore
