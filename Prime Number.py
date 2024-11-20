import math

def isPrime(n: int) -> bool:
    # Edge case for 1 as it's not a prime
    if n == 1:
        return False
    
    # Check divisibility from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
