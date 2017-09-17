import math
N = input()
moneys = []

for i in range(N):
    both = [int(x) for x in raw_input().split()]
    other_scores = [int(x) for x in raw_input().split()]

    above = 0
    for i in other_scores:
        if i > both[1]:
            above += 1

    moneys.append(math.sqrt(both[0] - above) * 100)

for i in moneys:
    print "Bob wins $%.2f at IOI!" % i
