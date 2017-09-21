casper, natalie = [], []

for i in range(input()):
    stats = [int(x) for x in raw_input().split()]
    casper.append(stats[0] * stats[1])

for i in range(input()):
    stats = [int(x) for x in raw_input().split()]
    natalie.append(stats[0] * stats[1])

if max(casper) > max(natalie):
    print "Casper"
elif max(natalie) > max(casper):
    print "Natalie"
else:
    print "Tie"


    
