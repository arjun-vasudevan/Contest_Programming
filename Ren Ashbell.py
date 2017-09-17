N = input()
power = []
condition = True

for i in range(N):
    power.append(input())

for i in power[1: len(power)]:
    if power[0] > i:
        continue
    else:
        condition = False
        break
if condition == True:
    print "YES"
else:
    print "NO"
