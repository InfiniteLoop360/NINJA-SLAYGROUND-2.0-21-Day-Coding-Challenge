def search(nums: [int], target: int) -> int:
    # Binary Search logic
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid  # Target found
        elif nums[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Target not found
