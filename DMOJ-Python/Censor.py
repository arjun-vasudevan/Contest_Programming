n = input()
sents = []
for i in range(n):
    sentence = raw_input().split()
    for i in sentence:
        if len(i) == 4:
            place = sentence.index(i)
            sentence.remove(i)
            sentence.insert(place, "****")
    sents.append(" ".join(sentence))

for i in sents:
    print i
