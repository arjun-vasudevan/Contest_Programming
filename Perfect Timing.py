import sys, datetime

x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
s = map(int, sys.stdin.readline().strip().split(':'))

a = datetime.datetime(s[0], s[1], s[2], s[3], s[4], s[5])
b = datetime.timedelta(seconds = abs(x2 - x1) + abs(y2 - y1))

print str(a + b).replace('-', ':').replace(' ', ':')
