admins = []
result = "NO"

for i in range(input()):
    person = raw_input().split()[1:]
    for i in person:
        for j in admins:
            if i in j:
                result = "YES"
    admins.append(person)

print result
