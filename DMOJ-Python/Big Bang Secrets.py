K = input()
P = 1
word = raw_input()
new_word = ""

for i in word:
    S = 3 * P + K
    letter = ord(i) - S
    if letter < 65:
        letter += 26
    new_word += chr(letter)
    P += 1

print new_word
