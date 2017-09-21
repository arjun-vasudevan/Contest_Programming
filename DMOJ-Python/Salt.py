from sys import stdin

N, Q = map(int, stdin.readline().split())
x_co, y_co = {}, {}

for _ in xrange(N):
    x, y = map(int, stdin.readline().split())
    if x in x_co:
        x_co[x].append(y)
    else:
        x_co[x] = [y]

    if y in y_co:
        y_co[y].append(x)
    else:
        y_co[y] = [x]
    
for _ in xrange(Q):
    q = stdin.readline().split()
    
    if q[0] == '1':
        if int(q[1]) in x_co:
            if int(q[2]) in x_co[int(q[1])]:
                print 'salty'
            else:
                print 'bland'
        else:
            print 'bland'
            
    elif q[1] == 'X':
        if int(q[2]) in x_co:
            print len(x_co[int(q[2])])
        else:
            print 0
    else:
        if int(q[2]) in y_co:
            print len(y_co[int(q[2])])
        else:
            print 0
