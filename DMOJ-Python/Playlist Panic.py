songs = []

for i in range(input() + 1):
    time = raw_input().split()
    songs.append(int(time[0]) * 60 + int(time[1]))

total, count = 0, 0
for i in sorted(songs[:-1]):
    if (total + i) <= songs[-1]:
        total += i
        count += 1

print count
