import random

# # random.seed(666) -- any number works.
L = [random.randint(-1_000_000, 1_000_000) for _ in range(1_000_000)]

# Finding the minimum value in the list.
def search_min(L):
    min_value = L[0]
    idx = 0
    counter = 1
    
    while counter < len(L): # Could try [<= len(L) - 1] as well
        v = L[counter]
        if v < min_value:
            min_value = v
            idx = counter
        else:
            pass
        counter += 1
        
    return min_value, idx   

print()         
print("Outcome following the pseudocode:", search_min(L))

# Finding the minimum value in the list and its index using enumerate()
def search_min_enum(L):
    min_value = L[0]
    min_index = 0
    
    for i, v in enumerate(L):
        if v < min_value:
            min_value = v
            min_index = i
            
    return min_value, min_index

print("Outcome using the enumerate function:", search_min_enum(L))


# Using the lambda, min, and enumerate functions
min_index, min_value = min(enumerate(L), key=lambda x: x[1])
print("Using the min and enumerate functions:", min_value, min_index)


# Using min() and .index()
min_value = min(L)
min_index = L.index(min_value)
print("Using the min and .index functions:", min_value, min_index)

print()
print(min(L))
# print(list(enumerate(L))) -- don't try it; it's a very long list.

