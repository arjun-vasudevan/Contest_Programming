from sys import stdin

L = int(stdin.readline())
start, to_print = '', []

for i in stdin.readline():
    if i == 'O':
        start += i
    else:
        if start != '':
            to_print.append(start)
        start = ''

print len(to_print)
if to_print:
    for i in to_print:
        print i
