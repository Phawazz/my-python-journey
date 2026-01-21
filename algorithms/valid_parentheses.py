def is_valid(brac): 
    bracket_map = { "]" : "[", ")" : "(", "}" : "{"}
        # Mapping closing to opening brackets with a dictionary
    
    store = []
    
    for i in brac:
    # Check if it's an opening bracket (Value)
        if i in bracket_map.values():
            store.append(i)

        # Check if it's a closing bracket (Key)
        elif i in bracket_map:
        # automatically false if closing bracket will be the first item
            if len(store) == 0:
                return False
            
            last_i = store.pop()
            
            # Checking for mismatch
            if bracket_map[i] != last_i:
                return False
        
    return len(store) == 0
    # After the whole code runs, an empty list indicates a valid parentheses and thereby returns True, otherwise, False is returned.
    
test_cases = ["()[]{}", "{[()]}", "(]", "]", "(()"]

for t in test_cases:
    print(f"Input: {t} \t -> {is_valid(t)}")
