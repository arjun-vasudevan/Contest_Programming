import math

N = input()
courses = {}

for i in range(N):
    course, avg = raw_input().split()
    courses[course] = float(avg[:-1])

to_drop = raw_input()

# Output 1 ----------
print format(sum(courses.values()) / N, ".2f") + "%"

# Output 2 ----------
total = 0
for i in courses.keys():
    if i != to_drop:
        total += courses[i]
print format(total / (N - 1), ".2f") + "%"

# Output 3 ----------
optimal_drop = min(courses, key = courses.get)
print optimal_drop

# Output 4 ----------
total = 0
for i in courses.keys():
    if i != optimal_drop:
        total += courses[i]
third_avg = total / (N - 1)
print format(third_avg, ".2f") + "%"

# Output 5 ----------
if third_avg >= 95:
    print "You have reached your goal."
else:
    diff = str(int(math.floor(95 - third_avg)))
    print "You are " + diff + "% away from your goal."
