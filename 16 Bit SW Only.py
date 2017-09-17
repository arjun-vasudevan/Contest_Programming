for _ in xrange(input()):
    nums = map(int, raw_input().split())
    print 'POSSIBLE DOUBLE SIGMA' if nums[0] * nums[1] == nums[2] else '16 BIT S/W ONLY'
