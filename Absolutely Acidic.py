from collections import Counter
from sys import stdin

max_diff = 0

readings = [int(stdin.readline()) for _ in range(int(stdin.readline()))]

counts = Counter(readings)
most_max = max([x for x in counts if counts[x] == max(counts.values())])

new_readings = filter(lambda a: a != most_max, readings)

counts = Counter(new_readings)
for i in [x for x in counts if counts[x] == max(counts.values())]:
    if abs(i - most_max) > max_diff:
        max_diff = abs(i - most_max)

print max_diff
