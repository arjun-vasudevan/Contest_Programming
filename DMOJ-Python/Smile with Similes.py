numAdjs = input()
numNouns = input()

adjs = []
nouns = []
for i in range(numAdjs):
    adjs.append(raw_input())
for j in range(numNouns):
    nouns.append(raw_input())
for adjective in adjs:
    for noun in nouns:
        print adjective + " as " + noun
