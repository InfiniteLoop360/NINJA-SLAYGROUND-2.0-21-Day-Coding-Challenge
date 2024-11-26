from typing import List
from collections import Counter

def getFrequencies(v: List[int]) -> List[int]:
    # Count the frequency of each element
    freq = Counter(v)
    
    # Determine the element with the highest frequency
    max_freq = max(freq.values())
    max_freq_elements = [key for key, value in freq.items() if value == max_freq]
    max_freq_element = min(max_freq_elements)  # Pick the smallest element
    
    # Determine the element with the lowest frequency
    min_freq = min(freq.values())
    min_freq_elements = [key for key, value in freq.items() if value == min_freq]
    min_freq_element = min(min_freq_elements)  # Pick the smallest element
    
    return [max_freq_element, min_freq_element]
