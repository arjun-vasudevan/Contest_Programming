sets = input()
sentences = []

for i in range(sets):
    s, v, o = input(), input(), input()
    subjects = [raw_input() for x in range(s)]
    verbs = [raw_input() for y in range(v)]
    objects = [raw_input() for z in range(o)]

    for m in subjects:
        for n in verbs:
            for o in objects:
                sentences.append(m + " " + n + " " + o + ".")

for i in sentences:
    print i
