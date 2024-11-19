from math import *
from collections import *
from sys import *
from os import *

def nthFibonacci(n):
    # Edge cases for the first two Fibonacci numbers
    if n == 1 or n == 2:
        return 1

    # Initialize the first two Fibonacci numbers
    prev1, prev2 = 1, 1

    # Compute the nth Fibonacci number iteratively
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev1, prev2 = prev2, curr

    return curr

# Input as specified in the question
n = int(input())
print(nthFibonacci(n))
