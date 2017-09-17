from sys import stdin

pos, neg, zero = [], [], False

for _ in xrange(int(stdin.readline())):
    num = int(stdin.readline())
    if num > 0:
        pos.append(num)
    elif num < 0:
        neg.append(num)
    else:
        zero = True

prod = 1

if pos:
    prod *= reduce(lambda x, y: x * y, pos)
    if neg:
        neg.sort()
        if len(neg) == 1:
            if zero:
                prod *= 0
            else:
                prod *= neg[0]
        elif len(neg) % 2 == 0:
            prod *= reduce(lambda x, y: x * y, neg)
        else:
            prod *= reduce(lambda x, y: x * y, neg[:-1])
else:
    if neg:
        neg.sort()
        if len(neg) == 1:
            if zero:
                prod *= 0
            else:
                prod *= neg[0]
        elif len(neg) % 2 == 0:
            prod *= reduce(lambda x, y: x * y, neg)
        else:
            prod *= reduce(lambda x, y: x * y, neg[:-1])
    else:
        prod = 0

print prod
