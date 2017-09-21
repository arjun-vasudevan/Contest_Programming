numPhone = input()
phoneNumbers = []

for i in range(numPhone):
    phoneNumbers.append(raw_input())

for number in phoneNumbers:
    if len(number) > 10 or len(number) < 10:
        print "not a phone number"
    else:
        if number[0] == "4" and number[1] == "1" and number[2] == "6" or number[0] == "6" and number[1] == "4" and number[2] == "7":
            number = "(" + number[0] + number[1] + number[2] + ")" + "-" + number[3] + number[4] + number[5] + "-" + number[6] + number[7] + number[8] + number[9]
            print number
        else:
            print "not a phone number"
