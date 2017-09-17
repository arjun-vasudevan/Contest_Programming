import sys

N, K = int(sys.stdin.readline()), int(sys.stdin.readline())
groups = N // K

if groups == 0:
    print K - N
else:
    if N % K == 0:
        print 0
    else:
        count_out = N - (groups * K)
        add = ((groups + 1) * K) - N
        print min(count_out, add)
