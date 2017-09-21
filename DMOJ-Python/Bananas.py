def check_Aword(word):
    if word == 'A':
        return True
    
    if len(word) >= 2:
        return True if (word[0] == 'B' and word[-1] == 'S' and check_monkey(word[1:-1])) else False
    
    return False

def check_monkey(word):
    if check_Aword(word):
        return True

    for i in xrange(1, len(word) - 1):
        if word[i] == 'N' and check_Aword(word[:i]) and check_monkey(word[i + 1:]):
            return True
        
    return False

word = raw_input()
while word != 'X':
    print 'YES' if check_monkey(word) else 'NO'
    word = raw_input()
