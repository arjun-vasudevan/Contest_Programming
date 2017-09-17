N = input()
mangas = []
prices = []

for i in range(N):
    both = raw_input()
    both = both.split()
    mangas.append(both[0])
    prices.append(float(both[1]))

cheap = prices.index(max(prices))
print mangas[cheap]
