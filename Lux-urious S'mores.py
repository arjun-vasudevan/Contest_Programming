from sys import stdin

N, K, L = map(int, stdin.readline().rstrip('\n').split())
fires = [int(stdin.readline()) for _ in xrange(N)]
count = 0

for ind, item in enumerate(fires):
    behind = ind - 1
    ahead = ind + 1
    if ahead == len(fires):
        ahead = 0

    if (item >= K and max(abs(item - fires[behind]), abs(fires[ahead] - item)) > L) or (item < K and max(abs(item - fires[behind]), abs(fires[ahead] - item)) <= L):
        count += 1

print count
