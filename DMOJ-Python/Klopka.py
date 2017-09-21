N = input()
x_coords = []
y_coords = []

for i in range(N):
    pos = [int(x) for x in raw_input().split()]
    x_coords.append(pos[0])
    y_coords.append(pos[1])

x_coords.sort()
y_coords.sort()

if x_coords[-1] - x_coords[0] > y_coords[-1] - y_coords[0]:
    print (x_coords[-1] - x_coords[0]) ** 2
else:
    print (y_coords[-1] - y_coords[0]) ** 2
