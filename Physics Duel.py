import sys, math

h = 0
for i in range(int(sys.stdin.readline())):
    s, x, t = [float(_) for _ in sys.stdin.readline()[:-1].split()]
    h += t * s * math.sin(x * math.pi / 180.0)

print int(round((2 * 9.8 * h) ** 0.5))
