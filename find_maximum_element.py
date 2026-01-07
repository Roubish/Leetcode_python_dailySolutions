# Find the maximum element in an array.

#stat with first element as the currect maximum
# compare the each elenment with the current maximum
# update the maximum if a larger element in found
# At the end, return the maximum element

def find_max(arr):
    max_val = arr[0]
    for num in arr:         # 1
        if num > max_val:
              max_val = num
    return max_val

arr = [3, 1, 7, 4, 9, 2]

print(find_max(arr))

# O(n)time, O(1) space 