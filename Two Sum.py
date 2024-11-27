from typing import List

def read(n: int, book: List[int], target: int) -> str:
    # Create a set to store visited book pages
    visited = set()
    
    # Traverse through each book
    for pages in book:
        # Calculate the required pages to reach target
        required = target - pages
        
        # If the required pages are already in visited set, return "YES"
        if required in visited:
            return "YES"
        
        # Otherwise, add the current pages to the visited set
        visited.add(pages)
    
    # If no pair found, return "NO"
    return "NO"
