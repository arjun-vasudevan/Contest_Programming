H = input()

for i in range(1, H, 2):
    line = ("*" * i) + (" " * (H - i))
    line += line[::-1]
    print line

print "*" * (2 * H)

for i in range(H - 2, 0, -2):
    line = ("*" * i) + (" " * (H - i))
    line += line[::-1]
    print line
