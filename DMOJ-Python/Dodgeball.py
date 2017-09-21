from sys import stdin

N = int(stdin.readline())
names = stdin.readline().split()

letter = ''
combs, occs = 0, 0

for i in names:
    if i[0] == letter:
        occs += 1
    else:
        letter = i[0]
        occs = 1
    combs += occs
    
print combs
