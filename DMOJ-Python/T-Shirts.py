from sys import stdin

S, M, L = map(int, stdin.readline().split())
A, B, C = map(float, stdin.readline().split())

count, cost = 0, 0
while S != 0 or M != 0 or L != 0:
    if S != 0:
        S -= 1
        cost += A
    elif M != 0:
        M -= 1
        cost += B
    elif L != 0:
        L -= 1
        cost += C
    count += 1

    if count == 3:
        if L != 0:
            L -= 1
        elif M != 0:
            M -= 1
        elif S != 0:
            S -= 1
        count = 0

print format(cost, '.2f')
