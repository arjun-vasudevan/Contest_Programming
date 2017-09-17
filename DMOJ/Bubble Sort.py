import sys
N = int(sys.stdin.readline())
nums = [int(x) for x in sys.stdin.readline()[:-1].split()]
sorts = sorted(nums)

print ' '.join(map(str, nums))

place = 0
while nums != sorts:
    if place < N - 1:
        if nums[place] > nums[place + 1]:
            temp = nums[place]
            nums[place] = nums[place + 1]
            nums[place + 1] = temp
            print ' '.join(map(str, nums))
        place += 1
    else:
        place = 0
