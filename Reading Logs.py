from sys import stdin

D, P, code = int(stdin.readline()), int(stdin.readline()), stdin.readline().rstrip()

perfect = round(P / float(D))
people, order = [], []

for _ in xrange(int(stdin.readline())):
    name, rate, course = stdin.readline().rstrip().split()
    
    if course == code:
        people.append((int(rate), name))
        order.append(name)

people.sort(reverse = True)
maxes = [x[1] for x in people if x[0] == people[-1][0]]
maxes.sort(key = lambda x: order.index(x))

if not people:
    print 'None of the readers are perfectly efficient.'
elif len(maxes) == 1:
    print 'The most efficient reader is ' + maxes[0] + '.'
    
    if people[-1][0] == perfect:
        print 'This reader is perfectly efficient.'
    else:
        print 'None of the readers are perfectly efficient.'
else:
    print 'The most efficient readers are ' + ','.join(maxes) + '.'
    
    if people[-1][0] == perfect:
        print 'These readers are perfectly efficient.'
    else:
        print 'None of the readers are perfectly efficient.'
