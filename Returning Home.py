a = True
direc = []
street = []
while a == True:
    turn = raw_input()
    road = raw_input()
    if road != "SCHOOL":
        direc.append(turn)
        street.append(road)
    else:
        a = False
        direc.append(turn)
        direc.reverse()
        street.reverse()

for i in range(len(street)):
    if direc[i] == "L":
        print "Turn RIGHT onto " + street[i] + " street."
    else:
        print "Turn LEFT onto " + street[i] + " street."

if direc[-1] == "L":
    print "Turn RIGHT into your HOME."
else:
    print "Turn LEFT into your HOME."
