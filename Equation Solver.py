equation = raw_input().split()
for n,i in enumerate(equation):
    if i == "P":
        equation[n] = "+"
    if i == "M":
        equation[n] = "-"

equation = ''.join(equation[:-1])

print eval(equation)
