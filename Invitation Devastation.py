template = raw_input("")
numPeople = input("")
names = []

for i in range(numPeople):
    names.append(raw_input(""))
    
for j in range(numPeople):
    print template.replace(">", names[j])
