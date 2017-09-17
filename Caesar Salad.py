from sys import stdin

ingre = 'abcdefghijklmnopqrstuvwxyz'
salad = 'abceglor'

for _ in range(int(stdin.readline())):
    info = stdin.readline().rstrip().split()

    for i in xrange(26):
        temp = map(list, zip(list(info[1].lower()), map(int, info[2:])))
        for ind, char in enumerate(temp):
            temp[ind][0] = ingre[(ingre.index(char[0]) + (char[1] * i)) % 26]

        for j in [x[0] for x in temp]:
            if j not in salad:
                break
        else:
            print i
            break
    else:
        print -1
