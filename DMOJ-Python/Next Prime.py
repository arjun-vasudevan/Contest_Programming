import sys
import math

def is_prime(num):
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True
    elif num % 2 != 0: 
        divisors = [int(x) for x in xrange(1, int(math.ceil(num**0.5))) if num % x == 0]
        if len(divisors) + 1 == 2:
            return True
        
    return False

num = int(sys.stdin.readline())
next_prime = []

while len(next_prime) == 0:
    if is_prime(num):
        next_prime.append(num)
    num += 1

print next_prime[0]
