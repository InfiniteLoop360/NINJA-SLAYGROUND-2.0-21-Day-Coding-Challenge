from os import *
from sys import *
from collections import *
from math import *

def addOneToNumber(arr):
    # Start from the end of the array to handle carry
    n = len(arr)
    carry = 1  # Start with adding 1
    for i in range(n - 1, -1, -1):
        arr[i] += carry
        if arr[i] < 10:  # No carry required
            carry = 0
            break
        else:  # Handle carry
            arr[i] = 0
            carry = 1
    
    # If carry is still left, add it to the front
    if carry == 1:
        arr.insert(0, 1)
    
    # Remove leading zeros if any
    while len(arr) > 1 and arr[0] == 0:
        arr.pop(0)
    
    return arr
