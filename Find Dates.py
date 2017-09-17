import sys
import re

numDays = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
to_print = []

def check_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

def check_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

for i in range(input()):
    sentence = raw_input().split()
    for word in sentence:
        date = re.sub('[^0-9-]', '', word).split("-")
        
        if len(date) == 3 and check_int(date[0]) and check_int(date[1]) and check_int(date[2]):
            if len(date[0]) == 4 and len(date[1]) == 2 and len(date[2]) == 2:
                year = int(date[0])
                month = int(date[1])
                day = int(date[2])
                if check_leap(year):
                    if month <= 12:
                        if month == 2:
                            if day <= numDays.get(month) + 1:
                                to_print.append("-".join(date))
                        else:
                            if day <= numDays.get(month):
                                to_print.append("-".join(date))
                else:
                    if month <= 12:
                        if day <= numDays.get(month):
                            to_print.append("-".join(date))

for i in to_print:
    print i
