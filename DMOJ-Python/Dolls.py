from sys import stdin
from collections import Counter

N = stdin.readline()
counts = Counter(map(int, stdin.readline().split()))

print abs(max([x for x in counts if counts[x] == max(counts.values())]) - min([x for x in counts if counts[x] == min(counts.values())]))
