from sys import stdin

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

for _ in xrange(int(stdin.readline())):
    n = int(stdin.readline())

    if n <= 33:
        print fact(n)
    else:
        print 0
