word = raw_input()
new_words = []

while word != "quit!":
    if len(word) > 4 and (word[-3] not in "aeiou") and word[-2] == "o":
        new_words.append(word[:-2] + "our")
    else:
        new_words.append(word)
    word = raw_input()

for i in new_words:
    print i
