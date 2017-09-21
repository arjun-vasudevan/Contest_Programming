words = {}
count = 0

for i in range(input()):
    word = raw_input()
    words[word] = words.get(word, 0) + 1

for i in words.keys():
    if words[i] == 1:
        count += 1

print count
        
