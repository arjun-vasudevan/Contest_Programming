Y = input()
a = True
b = True
    
while a == True:
    Y += 1
    lst = list(str(Y))
    for i in lst:
        if lst.count(i) == 1:
            b = True
        else:
            b = False
            break
        
    if b == True:
        print Y
        break
