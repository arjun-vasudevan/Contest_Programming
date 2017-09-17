stations = input()
stationsList = []
cond = False

for i in range(stations):
    stationsList.append(raw_input())
    
place = stationsList.index("Bessarion")

for i in stationsList:
    if i == "Bessarion":
        if (stationsList[place - 1] == "Leslie" and stationsList[place + 1] == "Bayview") or (stationsList[place - 1] == "Bayview" and stationsList[place + 1] == "Leslie"):
            cond = True
        else:
            cond = False 

if cond == False:
    print "N"
else:
    print "Y"
