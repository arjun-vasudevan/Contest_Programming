from sys import stdin

veterans = [stdin.readline().split() for _ in xrange(int(stdin.readline()))]
veterans.sort(key = lambda x: int(x[1]))

for new in xrange(int(stdin.readline())):
    s, d = map(int, stdin.readline().split())
    for expert in veterans:
        if int(expert[1]) >= s and int(expert[1]) <= s + d:
            print expert[0]
            break
    else:
        print 'No suitable teacher!'
