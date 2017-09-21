N = input()
nouns = []

for i in range(N):
    sentence = raw_input().split()
    count = 0
    for word in sentence:
        if word[0] == word[0].upper():
            count += 1
    nouns.append(count)

for i in nouns:
    print i
