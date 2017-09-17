N = input()
xy = [int(x) for x in raw_input().split()]
fe = [int(x) for x in raw_input().split()]
xy_score = 0
fe_score = 0

for i in range(N):
    if xy[i] > fe[i]:
        xy_score += 1
    elif xy[i] < fe[i]:
        fe_score += 1

print xy_score, fe_score
if xy_score > fe_score:
    print "Xyene"
elif fe_score > xy_score:
    print "FatalEagle"
else:
    print "Tie"
