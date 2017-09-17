keys = {'abc':2, 'def':3, 'ghi':4, 'jkl':5, 'mno':6, 'pqrs':7, 'tuv':8, 'wxyz':9}

word = raw_input()
while word != 'halt':
    group, time = '', 0
    
    for i in word:
        temp = [x for x in keys if i in x][0]
        if temp == group:
            time += 2
        time += temp.index(i) + 1
        group = temp

    print time
    
    word = raw_input()
