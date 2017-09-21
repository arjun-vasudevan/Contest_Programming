tile = 1
snakes = [[54, 19], [90, 48], [99, 77]]
ladders = [[40, 64], [9, 34], [67, 86]]

while tile != 100:
    dice = input()
    if dice == 0:
        print "You Quit!"
        break
    else:    
        if tile + dice <= 100:
            tile += dice
            
        for i in range(len(snakes)):
            if tile == snakes[i][0]:
                tile = snakes[i][1]
            elif tile == ladders[i][0]:
                tile = ladders[i][1]

        print "You are now on square", tile
        if tile == 100:
            print "You Win!"
            break
            
