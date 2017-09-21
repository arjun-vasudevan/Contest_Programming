info = [int(x) for x in raw_input().split()]
results = []

for i in range(info[0]):
    match = input()
    if match > ((info[1] ** 2 + info[2]**2)**0.5):
        results.append("NE")
    else:
        results.append("DA")
        
for i in results:
    print i
