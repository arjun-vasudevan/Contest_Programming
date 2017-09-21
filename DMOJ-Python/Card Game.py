import sys
cards = [sys.stdin.readline()[:-1] for x in range(52)]
A, B, high = 0, 0, "jackqueenkingace"

for i in range(52):
    if cards[i] == "ace" and len(cards[i + 1:]) >= 4:            
        if cards[i + 1] not in high and cards[i + 2] not in high and cards[i + 3] not in high and cards[i + 4] not in high:
            if i % 2 == 0:
                A += 4
                print "Player A scores 4 point(s)."
            else:
                B += 4
                print "Player B scores 4 point(s)."
    elif cards[i] == "king" and len(cards[i + 1:]) >= 3:            
        if cards[i + 1] not in high and cards[i + 2] not in high and cards[i + 3] not in high:
            if i % 2 == 0:  
                A += 3
                print "Player A scores 3 point(s)."
            else:
                B += 3
                print "Player B scores 3 point(s)."
    elif cards[i] == "queen" and len(cards[i + 1:]) >= 2:            
        if cards[i + 1] not in high and cards[i + 2] not in high:
            if i % 2 == 0:
                A += 2
                print "Player A scores 2 point(s)."
            else:
                B += 2
                print "Player B scores 2 point(s)."
    elif cards[i] == "jack" and len(cards[i + 1:]) >= 1:            
        if cards[i + 1] not in high:
            if i % 2 == 0:
                A += 1
                print "Player A scores 1 point(s)."
            else:
                B += 1
                print "Player B scores 1 point(s)."

print "Player A:", A, "point(s)."
print "Player B:", B, "point(s)."
