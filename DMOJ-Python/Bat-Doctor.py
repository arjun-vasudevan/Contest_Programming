import sys, math, re

num_rows, num_columns = map(int, sys.stdin.readline().split())
x_pos = []

for r in xrange(num_rows):
    row = sys.stdin.readline()
    for c in (x.start() for x in re.finditer('X', row)):
        x_pos.append((c, r))
x_pos.sort()

if len(x_pos) <= 1:
    print '0.000'
else:
    for i in xrange(len(x_pos) - 1):
        if x_pos[i][1] > x_pos[i + 1][1]:
            rise = x_pos[i][1] - x_pos[i + 1][1]
            run = x_pos[i + 1][0] - x_pos[i][0]
            theta = (math.atan(run / float(rise)) * 180 / math.pi)
            print format(theta, '.3f')
        elif x_pos[i][1] < x_pos[i + 1][1]:
            rise = x_pos[i + 1][1] - x_pos[i][1]
            run = x_pos[i + 1][0] - x_pos[i][0]
            theta = (math.atan(rise / float(run)) * 180 / math.pi)
            print format(theta + 90, '.3f')
        else:
            print '90.000'
