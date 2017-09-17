dimensions = [int(x) for x in raw_input().split()]
berries = 0
bush = []

for i in range(dimensions[1]):
    row = raw_input()
    berries += row.count("o")
    row = row.replace("*", " ")
    row = row.replace("o", " ")
    bush.append(row)

for i in bush:
    print i
print "o" * berries
