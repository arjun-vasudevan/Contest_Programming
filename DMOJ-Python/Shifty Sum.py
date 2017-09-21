N, k = input(), input()

shiftys = [N]

for i in range(k):
    N = int(str(N) + "0")
    shiftys.append(N)

print sum(shiftys)
