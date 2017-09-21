songs = ['A', 'B', 'C', 'D', 'E']

a = True
while a:
    b = input()
    for i in range(input()):
        if b == 1:
            songs.append(songs.pop(0))
        elif b == 2: 
            songs.insert(0, songs.pop(-1))
        elif b == 3:
            songs.insert(0, songs.pop(1))
        else:
            a = False

print ' '.join(songs)
