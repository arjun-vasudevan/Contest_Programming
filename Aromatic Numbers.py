aromatic = raw_input()
d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

calc = []

for i in range(1, len(aromatic) - 1, 2):
    if d[aromatic[i]] < d[aromatic[i + 2]]:
        calc.append(int(aromatic[i - 1]) * -1 * d[aromatic[i]])
    else:
        calc.append(int(aromatic[i - 1]) * d[aromatic[i]])
calc.append(int(aromatic[-2]) * d[aromatic[-1]])

print sum(calc)
