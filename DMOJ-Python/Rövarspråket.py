word = raw_input()
consonant =     "bcdfghjklmnpqrstvwxyz"
closestVowel =  "aaeeeiiiiooooouuuuuuu"
nextConsonant = "cdfghjklmnpqrstvwxyzz"
newWord = ""
for letter in word:
    if letter not in consonant:
        newWord += letter
    else:
        for i in range(len(consonant)):
            if letter == consonant[i]:
                letter = consonant[i] + closestVowel[i] + nextConsonant[i]
                newWord += letter

print newWord
