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
    
# Making the code above more pythonic

def same_case(a, b):
    # 1. Check if both are letters using .isalpha()
    if not a.isalpha() or not b.isalpha():
        return -1
    
    # 2. Check if their case matches
    # Since we know they are letters, we just compare their "islower" status
    if a.islower() == b.islower():
        return 1
    
    # 3. If they are letters but cases don't match
    return 0

# ==========================================
# Testing...
# ==========================================
if __name__ == "__main__":
    print("--- Testing same_case ---")
    print(f"'a', 'g' (Same lower): {same_case('a', 'g')} (Expected: 1)")
    print(f"'A', 'C' (Same upper): {same_case('A', 'C')} (Expected: 1)")
    print(f"'b', 'G' (Different):   {same_case('b', 'G')} (Expected: 0)")
    print(f"'B', 'g' (Different):   {same_case('B', 'g')} (Expected: 0)")
    print(f"'0', '?' (Not letters): {same_case('0', '?')} (Expected: -1)")