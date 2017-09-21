from sys import stdin

N = int(stdin.readline())
A, tot = [], 0

for pos, item in enumerate(map(int, stdin.readline().rstrip('\n').split())):
    if pos == 0:
        A.append(item)
        tot += item
        continue
    
    A.append(((pos + 1) * item) - tot)
    tot += A[-1]

print ' '.join(map(str, A))
