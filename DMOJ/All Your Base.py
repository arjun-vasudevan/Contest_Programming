from sys import stdin

def convert(number, base):
    digits = map(int, reversed(list(str(number))))
    
    dec_num = 0
    for pos, digit in enumerate(digits):
        dec_num += digit * (base ** pos)

    return dec_num

E, N = map(int, stdin.readline().split())
bases = map(int, stdin.readline().split())

rever = bases[::-1]
rever.append(E)

print reduce(lambda x, y: convert(y, x), rever)
