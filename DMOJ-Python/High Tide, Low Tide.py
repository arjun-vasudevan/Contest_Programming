from sys import stdin

N = int(stdin.readline())
measures = [int(_) for _ in stdin.readline()[:-1].split()]
measures.sort()

if N % 2 == 0:
    lows = measures[:N / 2][::-1]
    highs = measures[N / 2:]

    zipped = zip(lows, highs)
    to_print = ''
    
    for i in zipped:
        to_print += str(i[0]) + " " + str(i[1]) + " "

    print to_print[:-1]

else:
    lows = measures[:N / 2 + 1][::-1]
    highs = measures[N / 2 + 1:]
    
    zipped = zip(lows, highs)
    to_print = ''
    
    for i in zipped:
        to_print += str(i[0]) + " " + str(i[1]) + " "

    print to_print + str(lows[-1])
