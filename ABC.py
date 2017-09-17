nums = [int(x) for x in raw_input().split()]
nums.sort()
pos = raw_input()

d = {"A":nums[0], "B":nums[1], "C":nums[2]}

print d[pos[0]], d[pos[1]], d[pos[2]]
