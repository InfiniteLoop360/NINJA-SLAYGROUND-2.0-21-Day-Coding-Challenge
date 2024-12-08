
from typing import List

def merge_and_count(arr: List[int], temp: List[int], left: int, mid: int, right: int) -> int:
    i = left    # Starting index for the left subarray
    j = mid + 1 # Starting index for the right subarray
    k = left    # Starting index to be sorted
    inv_count = 0

    # Merge the two subarrays and count inversions
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)  # Count inversions
            j += 1
        k += 1

    # Copy the remaining elements of the left subarray, if any
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of the right subarray, if any
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        arr[i] = temp[i]

    return inv_count

def merge_sort_and_count(arr: List[int], temp: List[int], left: int, right: int) -> int:
    inv_count = 0
    if left < right:
        mid = (left + right) // 2

        inv_count += merge_sort_and_count(arr, temp, left, mid)
        inv_count += merge_sort_and_count(arr, temp, mid + 1, right)
        inv_count += merge_and_count(arr, temp, left, mid, right)

    return inv_count

def numberOfInversions(a: List[int], n: int) -> int:
    temp = [0] * n
    return merge_sort_and_count(a, temp, 0, n - 1)
