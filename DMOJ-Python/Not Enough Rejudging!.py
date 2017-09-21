import sys
status = ""

for i in range(int(sys.stdin.readline())):
    status += raw_input()

WA = int(0.3 * status.count("WA"))

status = status.replace("WA", "AC", WA)
status = status.replace("TLE", "WA")
status = status.replace("IR", "AC", 10)
status = status.replace("IR", "WA", 10)

to_print = map(''.join, zip(* [iter(status)] * 2))
for i in to_print:
    print i
