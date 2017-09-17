N = input("")
W = input("")
if W > 0:
    H = input("")
    print "It takes " + str((N * 6) + (((6-W) + 1) * H)) + " hours for Team 610 build a robot."
else:
    print "It takes " + str(N * 6) + " hours for Team 610 build a robot."
