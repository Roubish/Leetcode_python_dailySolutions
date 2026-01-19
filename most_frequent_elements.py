# Finde the top k frequent elements in an array.

# To solve this, count frequents with a hashmap then use a main-heap of size k (or use /
# bucket sort for 0(n)time) to retrieve the top k frequent elements.

# Counter (nums) builds a frequency map.
# Maintain a min-heap of size k keyed by frequency so the heap root is the courrent k-th most frequent element.
# For each (num, cnt), push until heap has k items; afterwards, only replace the root when you fined a higher frequency.
# At the end, the heap contains the top k frequent elements.

# Complexity:
    # Heap approach : O(n log k) space (for frequency map + heap of size k).
    # Bucket sort approch: O(n) time, O(n) space.

from collections import Counter
import  heapq

def top_k_frequent(nums, k):
    if k == 0:
        return []
    freq = Counter(nums) # here counting the "element -> count"
    heap = []   # size k 
    for num, cnt in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (cnt, num))
        else:
            if cnt > heap[0][0]:
                heapq.heapreplace(heap, (cnt, num))
    return [num for cnt, num in heap]

nums = [1,1,1,2,2,3,3,3,3,4]
print(top_k_frequent(nums, 2)) 

# Output 
# roubish@roubish-007:~/Documents/dsa_code_practice$ python3 most_frequent_elements.py 
# [1, 3]  
