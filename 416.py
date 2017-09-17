num = raw_input()

if num[:3] == "416":
    print "valuable"
elif num[:3] == "647" or num[:3] == "437":
    print "valueless"
else:
    print "invalid"
