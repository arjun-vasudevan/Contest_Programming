new_alpha = {'a':'@', 'b':'8', 'c':'(', 'd':'|)', 'e':'3', 'f':'#', 'g':'6', 'h':'[-]',
             'i':'|', 'j':'_|', 'k':'|<', 'l':'1', 'm':'[]\/[]', 'n':'[]\[]', 'o':'0', 'p':'|D',
             'q':'(,)', 'r':'|Z', 's':'$', 't':'\'][\'', 'u':'|_|', 'v':'\/', 'w':'\/\/', 'x':'}{', 'y':'`/', 'z':'2'}

new = ""
for i in list(raw_input().lower()):
    if i in new_alpha.keys():
        new += new_alpha[i]
    else:
        new += i

print new
