from sys import stdin

T = list(stdin.readline().rstrip()[1:])

for _ in xrange(int(stdin.readline())):
    string = list(stdin.readline().rstrip()[1:])
    for hole in T:
        if hole not in string:
            print 'no'
            break
    else:
        print 'yes'
