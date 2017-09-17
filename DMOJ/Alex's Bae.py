first = "".join(raw_input().lower().split())
second = "".join(raw_input().lower().split())

if len(first) == len(second) and sorted(first) == sorted(second):
    print "yes"
else:
    print "no"
