from sys import stdin
count = 0

for i in range(int(stdin.readline()), int(stdin.readline()) + 1):
    new = ''
    for j in str(i)[::-1]:
        if j in '18':
            new += j
        elif j == '6':
            new += '9'
        elif j == '9':
            new += '6'
        elif j == '0':
            new +='0'
        else:
            new = 'N'
            break
    if new != 'N':
        if int(new) == i:
            count += 1

print count
