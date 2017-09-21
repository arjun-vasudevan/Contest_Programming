from sys import stdin

des, elec, prog, bus, strat = [], [], [], [], []

for i in range(int(stdin.readline())):
    info = stdin.readline().rstrip('\n').split()
    rob_hrs = (float(info[4]) / 100.0) * int(info[5])
    if info[1] == 'Design':
        des.append((rob_hrs, info[0]))
    elif info[1] == 'Electrical':
        elec.append((rob_hrs, info[0]))
    elif info[1] == 'Programming':
        prog.append((rob_hrs, info[0]))
    elif info[1] == 'Business':
        bus.append((rob_hrs, info[0]))
    else:
        strat.append((rob_hrs, info[0]))

des_avg, elec_avg, prog_avg, bus_avg, start_avg = [0] * 5
if des:
    des_avg = sum([x[0] for x in des]) / float(len(des))
if elec:
    elec_avg = sum([x[0] for x in elec]) / float(len(elec))
if prog:
    prog_avg = sum([x[0] for x in prog]) / float(len(prog))
if bus:
    bus_avg = sum([x[0] for x in bus]) / float(len(bus))
if strat:    
    strat_avg = sum([x[0] for x in strat]) / float(len(strat))

print 'These Team Members Should Be Cut:'
print 'Design:'
for i in [x[1] for x in des if x[0] < des_avg]:
    print i
print ''
print 'Electrical:'
for i in [x[1] for x in elec if x[0] < elec_avg]:
    print i
print ''
print 'Programming:'
for i in [x[1] for x in prog if x[0] < prog_avg]:
    print i
print ''
print 'Business:'
for i in [x[1] for x in bus if x[0] < bus_avg]:
    print i
print ''
print 'Strategy:'
for i in [x[1] for x in strat if x[0] < strat_avg]:
    print i
