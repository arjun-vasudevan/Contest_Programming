N = input()
heights = []
counter = 0

for i in range(N):
    heights.append(input())

if heights[0] <= 41 and heights[1] <= 41:
    counter += 1

for i in range(1, N - 1):
    if heights[i-1] <= 41 and heights[i] <= 41 and heights[i+1] <= 41:
        counter += 1

if heights[N - 2] <= 41 and heights[N - 1] <= 41:
    counter += 1

print counter
