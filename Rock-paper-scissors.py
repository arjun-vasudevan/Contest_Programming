N = input()
alice, bob = [x for x in raw_input().split()], [x for x in raw_input().split()]
awin, bwin = 0, 0

for i in range(N):
    if (alice[i] == "rock" and bob[i] == "scissors") or (alice[i] == "paper" and bob[i] == "rock") or (alice[i] == "scissors" and bob[i] == "paper"):
        awin += 1
    elif (alice[i] == "rock" and bob[i] == "paper") or (alice[i] == "paper" and bob[i] == "scissors") or (alice[i] == "scissors" and bob[i] == "rock"):
        bwin += 1

print awin, bwin
