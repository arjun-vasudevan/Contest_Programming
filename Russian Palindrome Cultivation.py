from sys import stdin

def palin(val):
    if val == val[::-1]:
        return True
    return False

N = stdin.readline().rstrip('\n')

if N == '9' * len(N):
    print int(N) + 2
else:
    if len(N) % 2 == 0:
        first_half = N[:len(N) / 2]
        new = first_half + first_half[::-1]

        if new <= N:
            first_half = str(int(first_half) + 1)
            new = first_half + first_half[::-1]
    else:
        first_part = N[:len(N) / 2]
        second_part = first_part[::-1]
        new = first_part + N[len(N) / 2] + second_part

        if new <= N:
            new = first_part + str(int(N[len(N) / 2]) + 1) + second_part
            
    print new
