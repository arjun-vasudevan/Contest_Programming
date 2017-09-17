c, r = [int(m) for m in raw_input().split()]
points = []
x, y = 0, 0

co_ord = raw_input().split()
while co_ord != ['0', '0']:
    points.append([int(a) for a in co_ord])
    co_ord = raw_input().split()

for i in points:
    x += i[0]
    y += i[1]
    
    if x > c:
        x = c
    elif x < 0:
        x = 0
        
    if y > r:
        y = r
    elif y < 0:
        y = 0
    
    print x, y
