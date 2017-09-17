line1 = [int(x) for x in raw_input().split()]
line2 = [int(x) for x in raw_input().split()]
line3 = [int(x) for x in raw_input().split()]
line4 = [int(x) for x in raw_input().split()]
cond = True
magic = line1[0] + line2[0] + line3[0] + line4[0]
for i in range(4):
    if line1[i] + line2[i] + line3[i] + line4[i] != magic:
        cond = False

if sum(line1) != magic or sum(line2) != magic or sum(line3) != magic or sum(line4) != magic:
    cond = False

if cond == False:
    print "not magic"
else:
    print "magic"
