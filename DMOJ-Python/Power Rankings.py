N, P = [int(x) for x in raw_input().split()]

names = [raw_input() for x in range(N)]
powerpoints = [[int(x) for x in raw_input().split()] for y in range(P)]

times = []

for i in range(len(names)):
    time = 0
    for j in range(len(powerpoints)):
        time += powerpoints[j][i]

    times.append([time, names[i]])

times.sort()
times.reverse()

for i in range(3, len(times) + 3):
    print str(i) + ". " + times[i - 3][1]
