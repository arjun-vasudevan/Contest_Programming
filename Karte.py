import sys

d = {"P":0, "K":0, "H":0, "T":0}

deck = map(''.join, zip(*[iter(sys.stdin.readline())]*3))
result = ""

P = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
K = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
H = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']
T = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13']

for i in deck:
    suit = i[0]
    num = i[1:]

    if suit == "P":
        if num not in P:
            result = "GRESKA"
            break
        else:
            P.remove(num)
    elif suit == "K":
        if num not in K:
            result = "GRESKA"
            break
        else:
            K.remove(num)
    elif suit == "H":
        if num not in H:
            result = "GRESKA"
            break
        else:
            H.remove(num)
    else:
        if num not in T:
            result = "GRESKA"
            break
        else:
            T.remove(num)
            
    d[suit] = d.get(suit, 0) + 1

if result == "GRESKA":
    print "GRESKA"
else:
    print 13 - d["P"], 13 - d["K"], 13 - d["H"], 13 - d["T"]
