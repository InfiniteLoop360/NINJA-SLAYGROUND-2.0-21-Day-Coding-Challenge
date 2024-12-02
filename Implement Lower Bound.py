def lowerBound(arr: [int], n: int, x: int) -> int:
    # Initialize search bounds
    left, right = 0, n
    
    # Binary search for the lower bound
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < x:
            left = mid + 1
        else:
            right = mid
    
    return left

