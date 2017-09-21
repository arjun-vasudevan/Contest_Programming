from sys import stdin
string = stdin.readline()

indices = [[int(x) for x in stdin.readline().split()] for _ in range(int(stdin.readline()))]

counts = [0]
for i in string:
    if i == "G":
        counts.append(counts[-1] + 1)
    else:
        counts.append(counts[-1])
    
for i in indices:
    print counts[i[1] + 1] - counts[i[0]]
