from sys import stdin

J, A = input(), input()

sizes = [stdin.readline().strip() for _ in xrange(J)]

tot = 0
for _ in xrange(A):
    size, num = stdin.readline().strip().split()
    num = int(num) - 1
    if sizes[num] != None:
        if size == 'S' or (size == 'M' and sizes[num] in 'ML') or size == sizes[num] == 'L':
            tot += 1
            sizes[num] = None

print tot
