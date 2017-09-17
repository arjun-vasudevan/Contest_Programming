owed, debt = [0], 0

for _ in range(input()):
    query = raw_input().split()
    if query[0] == 'borrow':
        debt += int(query[1])
    else:
        debt -= int(query[1])

    owed.append(debt)

print owed.index(max(owed))
