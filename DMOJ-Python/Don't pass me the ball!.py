J = input()

if J < 4:
    print 0
elif J == 4:
    print 1
else:
    J -= 3
    print (J * (J + 1) * (J + 2)) / 6
