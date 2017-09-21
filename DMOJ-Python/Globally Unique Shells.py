from sys import stdin

N = int(stdin.readline())
A, B = [int(_) for _ in stdin.readline()[:-1].split()]

print N - len(list(set([int(_) for _ in stdin.readline()[:-1].split()]).intersection([int(_) for _ in stdin.readline()[:-1].split()])))
