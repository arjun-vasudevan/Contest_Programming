general, girls, teams = [], [], []

for i in range(input()):
    name, kind, points = raw_input().split()
    
    general.append([int(points), name])
    if kind == "girls":
        girls.append([int(points), name])

general.sort()
girls.sort()

if len(general) == 1:
    teams.append(general[-1][1])
elif len(general) != 0:
    teams.append(general[-1][1])
    teams.append(general[-2][1])

for i in range(len(girls) - 1, -1, -1):
    if girls[i][1] not in teams:
        teams.append(girls[i][1])
        break

teams.sort()

if len(teams) == 0:
    print "No ECOO :("
else:
    for i in teams:
        print i
