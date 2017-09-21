from sys import stdin

for _ in xrange(int(stdin.readline())):
    print ' '.join(['dank' if x == '1' else 'meme' for x in bin(int(stdin.readline()))[2:]])
