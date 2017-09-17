from sys import stdin

S, T = stdin.readline().rstrip(), stdin.readline().rstrip()
letters = 'abcdefghijklmnopqrstuvwxyz'

for shift in xrange(25, -1, -1):
    new = ''
    for char in S:
        new += letters[(letters.index(char) + shift) % 26]

    if T in new:
        print 0 if 26 - shift == 26 else 26 - shift
        print new
        break
