N = input()
lst = []

for i in range(N):
    lst.append(input())

for i in lst:
    divisors = []
    for j in range(1, i + 1):
        if i % j == 0:
            divisors.append(j)
    divisors.pop(-1)
    if sum(divisors) < i:
        print str(i) + " is a deficient number."
    elif sum(divisors) > i:
        print str(i) + " is an abundant number."
    else:
        print str(i) + " is a perfect number."
