code = {}

plain, cipher1, cipher2 = raw_input(), raw_input(), raw_input()
new = ""

for i in cipher1:
    code[i] = plain[cipher1.index(i)]

for i in cipher2:
    new += code.get(i, ".")

print new
