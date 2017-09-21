burgerChoices = {1: 461, 2:431, 3:420, 4:0}
sideChoices = {1:100, 2:57, 3:70, 4:0}
drinkChoices = {1:130, 2:160, 3:118, 4:0}
dessertChoices = {1:167, 2:266, 3:75, 4:0}

burger = input()
side = input()
drink = input()
dessert = input()

for i in range(1, 5):
    if burger != i:
        continue
    else:
        burger = burgerChoices[i]

for j in range(1, 5):
    if side != j:
        continue
    else:
        side = sideChoices[j]

for k in range(1, 5):
    if drink != k:
        continue
    else:
        drink = drinkChoices[k]

for l in range(1, 5):
    if dessert != l:
        continue
    else:
        dessert = dessertChoices[l]

print "Your total Calorie count is " + str(burger + side + drink + dessert) + "."
