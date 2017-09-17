n = input()

for i in range(n):
    birthday = [int(x) for x in raw_input().split()]
    if birthday[0] < 1989:
        print "Yes"
    elif birthday[0] > 1989:
        print "No"
    else:
        if birthday[1] < 2:
            print "Yes"
        elif birthday[1] > 2:
            print "No"
        else:
            if birthday[2] < 27:
                print "Yes"
            elif birthday[2] > 27:
                print "No"
            else:
                print "Yes"
