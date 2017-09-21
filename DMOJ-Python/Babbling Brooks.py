init_streams = [input() for x in range(input())]

action = input()

while action != 77:
    if action == 99:
        numSplit = input()
        percent = input() / 100.0

        if numSplit == len(init_streams) - 1:
            temp = init_streams[numSplit - 1]
            init_streams[numSplit - 1] = percent * init_streams[numSplit - 1]
            init_streams.append((1 - percent) * temp)
        else:
            temp = init_streams[numSplit - 1]
            init_streams[numSplit - 1] = percent * init_streams[numSplit - 1]
            init_streams.insert(numSplit, (1 - percent) * temp)
    else:
        numJoin = input()
        
        joined = init_streams[numJoin - 1] + init_streams[numJoin]
        del init_streams[numJoin]
        del init_streams[numJoin - 1]

        init_streams.insert(numJoin - 1, joined)

    action = input()

init_streams = [str(int(round(x))) for x in init_streams]
print " ".join(init_streams)
