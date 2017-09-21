size = input()
num = []

for i in range(size):
    num.append(input())
    num.sort()
for j in range(size):
    print min(num)
    num.remove(min(num))
