from sys import stdin
N = int(stdin.readline())

if N == 1:
    print 9
elif N == 17:
    print 99999998
elif N > 17:
    print 999999998
else:
    if N % 2 == 1:
        print int("10" + "9" * int(N / 2 - 1) + "8") % 1000000000
    else:
        print int("1" + "9" * int(N / 2 - 1) + "8") % 1000000000
