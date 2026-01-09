# Check if a string is a palindrome.
# To solve this, use Two pointers : one starting at the left end then other at the right end and compare characters until they meet.

# Palindrom reads the same froward and backward 
# Using two pointers compare chareters at the beginning and end 
# if all pairs match, it's a palindrome otherwise it's not 

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -=1 
    return True

print(is_palindrome("madam"))
print(is_palindrome("hello"))

# Complexity : O(n) time, O(1) space