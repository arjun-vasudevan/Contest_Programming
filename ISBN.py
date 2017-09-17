num1 = raw_input()
num2 = raw_input()
num3 = raw_input()
org = "9780921418" + num1 + num2 + num3
lst = []
sum1 = 0
sum2 = 0

for i in org:
    lst.append(i)

for digit in lst[0::2]:
    sum1 += int(digit) * 1

for digit in lst[1::2]:
    sum2 += int(digit) * 3

print "The 1-3-sum is", str(sum1 + sum2)
