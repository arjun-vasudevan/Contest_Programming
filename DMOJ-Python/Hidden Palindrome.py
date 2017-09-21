word = raw_input()

reverse = "".join(reversed(list(word)))
lengths = []
for i in range(len(word) + 1):
    for j in range(i + 1, len(word) + 1):
        if word[i:j] in reverse:
            lengths.append(len(word[i:j]))

print max(lengths)
