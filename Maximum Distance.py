from sys import stdin

for _ in xrange(int(stdin.readline())):
    n = int(stdin.readline())

    X = map(int, stdin.readline().split())
    Y = map(int, stdin.readline().split())

    dists = []

    for indx in xrange(n):
        for indy in xrange(n - 1, indx - 1, -1):
            if Y[indy] >= X[indx]:
                dists.append(indy - indx)
            else:
                dists.append(0)

    print 'The maximum distance is', max(dists)
