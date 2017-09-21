results = []

for i in range(input()):
    alpha = list("abcdefghijklmnopqrstuvwxyz")
    #temp = alpha
    sentence = list(raw_input().lower())
    diff = set(alpha) - set(sentence)
    if len(diff) == 0:
        results.append("pangram")
    else:
        missing = list(diff)
        missing.sort()
        results.append("missing " + ''.join(missing))
        
for i in results:
    print i
