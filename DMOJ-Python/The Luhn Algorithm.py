to_print = []

for i in range(5):
    nums = raw_input().split()
    last_digits = ""
    
    for i in nums:
        total = 0
        
        for j in i[::-2]:
            j = str(int(j) * 2)
            total += sum([int(x) for x in list(j)])

        for j in i[-2::-2]:
            total += int(j)

        for i in range(10):
            if (total + i) % 10 == 0:
                last_digits += str(i)
                break
    
    to_print.append(last_digits)

for i in to_print:
    print i
