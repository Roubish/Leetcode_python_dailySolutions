# Finde the length of the longest substring without repeating charaters.

# Explation 

# last_index remembers the most recent index of each character.
# start is left pointer of the current window (beginning of the substring without repeats).
# When a character repeats and its last seen insex is inside the window (>= start), move start to last_insex[ch] + 1 to exclude the earlier occurrence.
# Update last_index[ch] = i and compute the current window lenght i - start + 1. keep the maximum.
# Complexity : O(n)time, (min(n, E)) space where E is charactor alphabet size.


def longest_unique_substring(S):
    last_index = {} # store last index of each character 
    start = 0 # left boundary of windows
    max_len = 0

    for i, ch in enumerate(S):
        if ch in last_index and last_index[ch] >= start:
            start = last_index[ch] + 1
        last_index[ch] = i
        max_len = max(max_len, i - start +1)

    return max_len

print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("bbbbbb"))

# Output
# roubish@roubish-007:~/Documents/dsa_code_practice$ python3 longest_substring.py 
# 3
# 1
