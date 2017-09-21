pizza = []
for i in range(8):
    pizza.append(input())

sums = []
for j in range(8):
    if j <= 4:
        sums.append(pizza[j] + pizza[j+1] + pizza[j+2] + pizza[j+3])
    elif j == 5:
        sums.append(pizza[5] + pizza[6] + pizza[7] + pizza[0])
    elif j == 6:
        sums.append(pizza[6] + pizza[7] + pizza[0] + pizza[1])
    elif j == 7:
        sums.append(pizza[7] + pizza[0] + pizza[1] + pizza[2])

print max(sums)
