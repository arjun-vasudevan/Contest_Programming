numDays = input()
totals = []

for i in range(numDays):
    total = sum([input() for x in range(input())])
    totals.append(total)

for i in range(numDays):
    if totals[i] == 0:
        print "Weekend"
    else:
        print "Day " + str(i + 1) + ": " + str(totals[i])
