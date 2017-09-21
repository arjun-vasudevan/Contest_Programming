essay = raw_input()
new_essay = "".join(essay.split())

lower, upper = 0, 0

for letter in new_essay:
    if letter == letter.upper():
        upper += 1
    else:
        lower += 1

if upper > lower:
    print essay.upper()
elif lower > upper:
    print essay.lower()
else:
    print essay
        
