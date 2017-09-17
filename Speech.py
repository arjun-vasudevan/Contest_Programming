words = {}

for i in range(input()):
    both = raw_input().split()
    words[both[1]] = both[0]

speech = raw_input()
speech = speech.replace(".", "")
speech = speech.split()
new = []

for i in speech:
    if i in words.keys():
        new.append(words[i])
    else:
        new.append(i)

print " ".join(new) + "."
