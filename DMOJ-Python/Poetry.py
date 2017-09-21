def last_syllable(word):
    indexes = []
    for i in word:
        if i in "aeiou":
            indexes.append(word.rfind(i))
    if len(indexes) == 0:
        return word
    else:
        return word[max(indexes):]

poem, results = [], []

for i in range(input()):
    verse = [raw_input().lower().split()[-1] for x in range(4)]
    poem.append(verse)

for verse in poem:
    if last_syllable(verse[0]) == last_syllable(verse[1]) == last_syllable(verse[2]) == last_syllable(verse[3]):
        results.append("perfect")
    elif last_syllable(verse[0]) == last_syllable(verse[1]) and last_syllable(verse[2]) == last_syllable(verse[3]):
        results.append("even")
    elif last_syllable(verse[0]) == last_syllable(verse[2]) and last_syllable(verse[1]) == last_syllable(verse[3]):
        results.append("cross")
    elif last_syllable(verse[0]) == last_syllable(verse[3]) and last_syllable(verse[1]) == last_syllable(verse[2]):
        results.append("shell")
    else:
        results.append("free")
        
for i in results:
    print i
