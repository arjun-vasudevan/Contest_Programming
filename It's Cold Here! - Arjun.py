cities = {}
while True:
    both = raw_input().split()
    cities[both[0]] = int(both[1])
    if both[0] == "Waterloo":
        break

lst = sorted([(val, key) for key, val in cities.items()])
print lst[0][1]
