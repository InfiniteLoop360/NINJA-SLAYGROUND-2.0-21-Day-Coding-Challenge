def isSorted(n: int, a: [int]) -> int:
    # Iterate through the array starting from index 1
    for i in range(1, n):
        # If any element is smaller than the previous one, return 0
        if a[i] < a[i - 1]:
            return 0
    # If loop completes, the array is sorted, return 1
    return 1

