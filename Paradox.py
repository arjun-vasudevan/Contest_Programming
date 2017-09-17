C = input()

lst = []
to_print = []

def command1(item):
    if item not in lst:
        lst.append(item)
        return "true"
    else:
        return "false"

def command2(item):
    if item not in lst:
        return "false"
    else:
        lst.remove(item)
        return "true"

def command3(item):
    if item not in lst:
        return "-1"
    else:
        return str(lst.index(item))

for i in range(C):
    command = raw_input().split()
    if command[0] == '1':
        to_print.append(command1(command[1]))
    elif command[0] == '2':
        to_print.append(command2(command[1]))
    elif command[0] == '3':
        to_print.append(command3(command[1]))
    else:
        lst.sort()
        to_print.append(" ".join(lst))

for i in to_print:
    print i


