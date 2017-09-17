mom, dad = raw_input(), raw_input()

poss = ['a' if 'a' in mom and 'a' in dad else 'A']
poss.append('A') if 'A' in mom or 'A' in dad else 'a'

poss += ['b' if 'b' in mom and 'b' in dad else 'B']
poss.append('B') if 'B' in mom or 'B' in dad else 'b'

poss += ['c' if 'c' in mom and 'c' in dad else 'C']
poss.append('C') if 'C' in mom or 'C' in dad else 'c'

poss += ['d' if 'd' in mom and 'd' in dad else 'D']
poss.append('D') if 'D' in mom or 'D' in dad else 'd'

poss += ['e' if 'e' in mom and 'e' in dad else 'E']
poss.append('E') if 'E' in mom or 'E' in dad else 'e'

for _ in range(input()):
    for letter in raw_input():
        if letter not in poss:
            print 'Not their baby!'
            break
    else:
        print 'Possible baby.'
