from sys import stdin

k = int(stdin.readline())

for _ in xrange(k):
    print '*' * k + 'x' * k + '*' * k

for _ in xrange(k):
    print ' ' * k + 'xx' * k

for _ in xrange(k):
    print '*' * k + ' ' * k + '*' * k
