import sys

word = sys.stdin.readline()
string = int(sys.stdin.readline())

least = "zzzzzzzzzzzzzzzzzzzzzzzzz"

for i in range(len(word) - string):
    if word[i:i + string] < least:
        least = word[i:i + string]

print least
    
