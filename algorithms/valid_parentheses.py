def is_valid(brac): # FUNCTION is_valid is defined to determine whether a parenthesis is valid or not
    dic = {
        "]" : "[",
        ")" : "(",
        "}" : "{"
    } # a dictionary was created with the key:value pairs being the opening and closing brackets of the 3 types
    
    store = [] # an empty store was created
    
    for i in brac:
        if (i == "[" or i == "(" or i == "{"): 
            store.append(i)
        # This appends (, [, or { to the empty store above.
        
        elif (i == ")" or i == "]" or i == "}"):
            if len(store) == 0:
                return False
            last_i = store.pop()
            if dic[i] != last_i:
                return False
        # This block of code will pop out the previous item in the store if it comes across ), ], or } but will return False if no opening bracket has been pushed into store already, i.e. store is initially empty.

    if (len(store) != 0):
        return False
    return True
    # After the whole code runs, an empty list indicates a valid parentheses and thereby returns True, otherwise, False is returned.