word = raw_input()
results = []
count = 1
while word != "No More Words!":
    splitted = list(word)
    for i in range(1, len(word) - 1):
        if word[i-1] == "c" and word[i] == "i" and word[i+1] == "e":
            splitted[i] = "e"
            splitted[i+1] = "i"

        if word[i-1] != "c" and word[i] == "e" and word[i+1] == "i":
            splitted[i] = "i"
            splitted[i+1] = "e"

    if "".join(splitted) == word:
        results.append("Word " + str(count) + " is correct.")
    else:
        results.append("".join(splitted))
        
    count += 1
    word = raw_input()

for i in results:
    print i
    
