cases = {1:100, 2:500, 3:1000, 4:5000, 5:10000,
         6:25000, 7:50000, 8:100000, 9:500000, 10:1000000}

n = input()
unopened = range(1, 11)
for i in range(n):
    opened = input()
    unopened.remove(opened)
offer = input()
average = 0

for i in unopened:
    average += cases[i]

average /= len(unopened)

if average > offer:
    print "no deal"
else:
    print "deal"
