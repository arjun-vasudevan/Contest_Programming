from sys import stdin
 
sCount, tCount = 0, 0

for i in [stdin.readline() for _ in xrange(int(stdin.readline()))]:
    sCount += i.count('s') + i.count('S')
    tCount += i.count('t') + i.count('T')

print 'French' if sCount >= tCount else 'English'
