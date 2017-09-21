N = input()
tunnels = []

for i in range(N):
    tunnel = raw_input().split()
    tunnels.append(int(tunnel[1]) - int(tunnel[0]))

print max(tunnels)
