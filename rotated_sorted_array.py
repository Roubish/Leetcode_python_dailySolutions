# To solve this, use a modified binary search: determine which half is sorted and decide which side to continue serching.

def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:

            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search_rotated([4,5,6,7,0,1,2], 0))
print(search_rotated([4,5,6,7,0,1,2], 3))


# use binery search to get O(log n) time At each step, check which side (left-> mid or mid -> right) is normally sirted by comparing endpoint values.


# Output
# roubish@roubish-007:~/Documents/dsa_code_practice$ python3 rotated_sorted_array.py 
# 4
# roubish@roubish-007:~/Documents/dsa_code_practice$ python3 rotated_sorted_array.py 
# 4
# -1