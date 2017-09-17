import sys

to_print = []

A = int(sys.stdin.readline())
while A != 0:
    l = int(A ** 0.5)

    while (A % l) != 0:
        l -= 1
    
    w = A / l

    P = int(2 * (l + w))
    
    to_print.append("Minimum perimeter is " + str(P) + " with dimensions " + str(l) + " x " + str(w))

    A = int(sys.stdin.readline())

for i in to_print:
    print i
