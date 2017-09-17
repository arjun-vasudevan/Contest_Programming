num = map(int, list(raw_input()))
print ''.join(map(str, sorted(num, reverse = True))) if sum(num) % 3 == 0 and 0 in num else -1
