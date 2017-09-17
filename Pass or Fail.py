from sys import stdin
import math

for _ in range(10):
    weights = map(int, stdin.readline().split())
    count = 0
    for student in range(int(stdin.readline())):
        average = 0
        person = map(int, stdin.readline().split())
        for i in range(4):
            average += ((weights[i] / 100.0) * person[i])

        if average > 49.9999:
            count += 1
    print count
