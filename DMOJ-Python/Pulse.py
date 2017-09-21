import sys
all_data = [int(x) for x in sys.stdin.readline().split()]
times = [int(sys.stdin.readline()) for x in range(all_data[0])]
count = 0

for i in times:
    if (i * 2) in range(all_data[1], all_data[2] + 1):
        count += 1

print count
