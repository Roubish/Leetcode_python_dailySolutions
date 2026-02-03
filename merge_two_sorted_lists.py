# Merge Two Sorted Lists
# Write a function to merge two sorted lists into one sorted list.


# Create a function that takes two sorted lists as input.
# This list will store the merged sorted result.
# These keep track of the current position in each list.
# Run a loop while both lists still have elements.
# Add the smaller element to the merged list and move that index forward.
# Once one list ends, add the leftover elements from the other list.
# return merge_list

def merge_sorted_list(lst1, lst2):
    merge_list = []
    i, j = 0, 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merge_list.append(lst1[i])
            i += 1
        else:
            merge_list.append(lst2[j])
            j += 1

    merge_list.extend(lst1[i:])
    merge_list.extend(lst2)
    return merge_list

print(merge_sorted_list([1, 3, 5], [2, 4, 6]))

# Outpust
# [1, 2, 3, 4, 5, 2, 4, 6]