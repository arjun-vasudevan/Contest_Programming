letters = {"A":"2", "B":"2", "C":"2", "D":"3", "E":"3", "F":"3", "G":"4", "H":"4",
           "I":"4", "J":"5", "K":"5", "L":"5", "M":"6", "N":"6", "O":"6", "P":"7",
           "Q":"7", "R":"7", "S":"7", "T":"8", "U":"8", "V":"8", "W":"9", "X":"9",
           "Y":"9", "Z":"9"}
t = input()
correct = []

for i in range(t):
    num = list(raw_input())
    num = [x for x in num if x != "-"]
    new = []      
    for val in num:
        if val in letters.keys():
            new.append(letters[val])
        else:
            new.append(val)
    new.insert(3, "-")
    new.insert(7, "-")
    new = "".join(new[:12])
    correct.append(new)

for i in correct:
    print i
