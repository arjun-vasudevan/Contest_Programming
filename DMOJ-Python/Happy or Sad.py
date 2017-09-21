line = raw_input("")

happyCount = line.count(":-)")
sadCount = line.count(":-(")

if happyCount == 0 and sadCount == 0:
    print "none"
elif happyCount > sadCount:
    print "happy"
elif happyCount < sadCount:
    print "sad"
elif happyCount == sadCount:
    print "unsure"
