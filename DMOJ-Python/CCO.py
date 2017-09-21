import sys

line1, line2, line3 = raw_input(), raw_input(), raw_input()
info = [int(x) for x in sys.stdin.readline().split()]

print "=" * (info[2]*2 + 5)
print "|" + str(info[0]) + (" " * (info[2]*2 + 3 - len(str(info[0])))) + "|"
for i in range(info[1] - 1):
    print "|" + (" " * (info[2]*2 + 3)) + "|"
print "|" + (" " * info[2]) + line1 + (" " * info[2]) + "|"
print "|" + (" " * info[2]) + line2 + (" " * info[2]) + "|"
print "|" + (" " * info[2]) + line3 + (" " * info[2]) + "|"
for i in range(info[1] - 1):
    print "|" + (" " * (info[2]*2 + 3)) + "|"
print "|" + (" " * (info[2]*2 + 3 - len(str(info[0])))) + str(info[0]) + "|"
print "=" * (info[2]*2 + 5)
