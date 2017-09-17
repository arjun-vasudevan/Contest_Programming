N = input()
marks = [input() for x in range(N)]
marks.sort()

if N % 2 == 1:
    print marks[N / 2]
else:
    median = (marks[N / 2] + marks[(N / 2) - 1]) / (2.0)
    print int(round(median))
