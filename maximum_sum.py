# Fine the maximum sum of any contiguous subarray of size k.

#Explanation ---
# Groups employees by department
# compite the sum of the elements as initial windows.
# For each next index i (from k to n-1) add arr[i] (new entering element) and subtract arr[i-k]
# (exiting element) to update window sum in O(1)
# Track the maximum window sum seen so far.
# Return the maximum after scanning once.
# Filters grous where the count of employees is more then 5.
## Complexity : O(n) time O(1) space.


# Solution 

def max_sum_subarray_k(arr, k):
    if k > len(arr) or k == 0:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray_k(arr, k))

# roubish@roubish-007:~/Documents/dsa_code_practice$ python3 maximum_sum.py 
# 9  # output is 9