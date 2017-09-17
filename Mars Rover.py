from sys import stdin

def commands():
    alls = []
    command = int(stdin.readline())
    while command != 0:
        alls.append(command)
        command = int(stdin.readline())
    return alls

n = int(stdin.readline())

for _ in xrange(n):
    ins = commands()
    x, y, d = 0, 0, 90

    straight = False
    for ind, comm in enumerate(ins):
        if straight:
            if d % 360 == 90:    y += comm
            elif d % 360 == 270: y -= comm
            elif d % 360 == 0:   x += comm
            else:                x -= comm
            straight = False
            continue

        if comm == 1:   straight = True
        elif comm == 2: d -= 90
        else:           d += 90

    print 'Distance is', abs(x) + abs(y)
    d %= 360
    
    back = []
    if x > 0:
        if y > 0:
            if d == 0:
                back = [2, 1, abs(y), 2, 1, abs(x)]
            elif d == 90:
                back = [3, 1, abs(x), 3, 1, abs(y)]
            elif d == 180:
                back = [1, abs(x), 3, 1, abs(y)]
            else:
                back = [1, abs(y), 2, 1, abs(x)]
        elif y < 0:
            if d == 0:
                back = [3, 1, abs(y), 3, 1, abs(x)]
            elif d == 90:
                back = [1, abs(y), 3, 1, abs(x)]
            elif d == 180:
                back = [1, abs(x), 2, 1, abs(y)]
            else:
                back = [2, 1, abs(x), 2, 1, abs(y)]
        else:
            if d == 0:
                back = [3, 3, 1, abs(x)]
            elif d == 90:
                back = [3, 1, abs(x)]
            elif d == 180:
                back = [1, abs(x)]
            else:
                back = [2, 1, abs(x)]
    elif x < 0:
        if y > 0:
            if d == 0:
                back = [1, abs(x), 2, 1, abs(y)]
            elif d == 90:
                back = [2, 1, abs(x), 2, 1, abs(y)]
            elif d == 180:
                back = [3, 1, abs(y), 3, 1, abs(x)]
            else:
                back = [1, abs(y), 2, 1, abs(x)]
        elif y < 0:
            if d == 0:
                back = [1, abs(x), 3, 1, abs(y)]
            elif d == 90:
                back = [1, abs(y), 2, 1, abs(x)]
            elif d == 180:
                back = [2, 1, abs(y), 2, 1, abs(x)]
            else:
                back = [3, 1, abs(x), 3, 1, abs(y)]
        else:
            if d == 0:
                back = [1, abs(x)]
            elif d == 90:
                back = [2, 1, abs(x)]
            elif d == 180:
                back = [3, 3, 1, abs(x)]
            else:
                back = [3, 1, abs(x)]
    else:
        if y > 0:
            if d == 0:
                back = [2, 1, abs(y)]
            elif d == 90:
                back = [3, 3, 1, abs(y)]
            elif d == 180:
                back = [3, 1, abs(y)]
            else:
                back = [1, abs(y)]
        elif y < 0:
            if d == 0:
                back = [3, 1, abs(y)]
            elif d == 90:
                back = [1, abs(y)]
            elif d == 180:
                back = [2, 1, abs(y)]
            else:
                back = [3, 3, 1, abs(y)]

    for i in back:
        print i

    if _ != n - 1:
        print ''
