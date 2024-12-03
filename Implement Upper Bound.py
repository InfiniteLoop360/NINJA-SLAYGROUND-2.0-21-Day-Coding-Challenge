def upperBound(arr: [int], x: int, n: int) -> int:
    low, high = 0, n
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] > x:
            high = mid
        else:
            low = mid + 1
    return low
