N = input()
alls = []

D = raw_input().split()
for i in D:
    if i not in alls:
        alls.append(i)

print(len(alls))
