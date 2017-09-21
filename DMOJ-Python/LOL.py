import sys

x, y = [], []

for i in range(int(sys.stdin.readline())):
    unit = [int(i) for i in sys.stdin.readline()[:-1].split()]
    x.append(unit[0])
    y.append(unit[1])

x.sort()
y.sort()

print (x[-1] - x[0]) * (y[-1] - y[0])
