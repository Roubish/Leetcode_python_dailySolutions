# Mearge all overlapping intervals in a list of intervals

# To solve this, sort intervals by start time, then iterate and mearge an interval with the previous one if the ovelap.

# sort intervals by their start times so potential overlaps are adjacent. 
# keep a mearge list with the last interval representing the current merged block.
# for each current intrval, check if current[0] <= last[1] (overlap) 
# if yes, extend last[1] = max(last[1], current[1]); otherwise append current as a new block.
# At the end, merged contains non-overlapping intervals covering all original intervals.

def merge_intervsls(intervals):
    if not intervals:
        return []
    
    intervals.sort(key = lambda X: X[0])
    merged = [intervals[0]]

    for current in intervals[1:]:

        last = merged[-1]
        if current[0] <= last[1]:

            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

intervals = [[1,3], [2,6], [8,10], [15,18]]
print(merge_intervsls(intervals))

# Output
# roubish@roubish-007:~/Documents/dsa_code_practice$ python3 mearge_all_overlapping_intervals.py 
# [[1, 6], [8, 10], [15, 18]]
