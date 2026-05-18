"""
    To merge overlapping meeting intervals after sorting by start/end time:

        Algorithm
        Sort intervals by start time (and end time if needed).
        Initialize result with the first interval.
        For each next interval:
        If it overlaps with the last merged interval:
        merge using end = max(current_end, new_end)
        Else:
        add as a new interval.
        Time Complexity
        Sorting: O(n log n)
        Merge traversal: O(n)
        Overall: O(n log n)
        Example

        Input:

        [[1,3],[2,6],[8,10],[15,18]]

        Sorted:

        [[1,3],[2,6],[8,10],[15,18]]

        Merged:

        [[1,6],[8,10],[15,18]]
"""

#Soulution 
def merge(intervals):
    intervals.sort(key = lambda x: (x[0], x[1]))
    
    merged = []
    
    for interval in intervals:
        
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged
    
intervals = [[1,3], [2,6], [8,10], [15, 18]]

print(merge(intervals))

# ghost@ghost-GF65-Thin-10UE:~/Documents/program_txt_folder/dsa_code$ python3 interval.py
# [[1, 6], [8, 10], [15, 18]]