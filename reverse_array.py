# Reverse an array in-place.

# arr = [1, 2, 3, 4, 5]
#print(reverse_array(arr)) # [5, 4, 3, 2, 1]

# Initialize two pointers: left at the start, right at the end.
# Swap array at the positions.
# Move left forward and right backward until they cross. # arr[left], arr[right] = arr[right], arr[left]
# array is reversed in-place, without using extra space.
# complexity O(n)time, 0(1) space.

def reverse_array(arr):
    left, right = 0, len(arr) -1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr = [1, 2, 3, 4, 5]
print(reverse_array(arr)) # [5, 4, 3, 2, 1]