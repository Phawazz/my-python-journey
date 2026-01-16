"""
Write a function that will check if two given characters are the same case.

If either of the characters is not a letter, return -1
If both characters are the same case, return 1
If both characters are letters, but not the same case, return 0
"""

def same_case(a, b):
    is_lower_a = 97 <= ord(a) <= 122 # Ord() returns the unicode integer equivalent of the character, and anything outside the 97-122 range isn't in lower case.
    is_upper_a = 65 <= ord(a) <= 90 # Just like the above, any value outside the 65-90 range isn't in upper case.
    is_lower_b = 97 <= ord(b) <= 122
    is_upper_b = 65 <= ord(b) <= 90
    
    if (is_lower_a and is_lower_b) or (is_upper_a and is_upper_b):
        return 1
    elif (is_lower_a and is_upper_b) or (is_upper_a and is_lower_b):
        return 0
    else:
        return -1 