import sys

to_print = []

for i in range(int(sys.stdin.readline())):
    number = int(sys.stdin.readline())
    if (number & number - 1 == 0):
        to_print.append("T")
    else:
        to_print.append("F")

for i in to_print:
    print i
