x = [12, 23, 34, 45, 56, 67, 78, 89, 90, 101, 123]
target = 23

# Recursive Implementation of Binary Search Algorithm
def binary_search_recur(items, target):
    
    mid = len(items) // 2
    
    if len(items) == 1:
        return mid if items[mid] == target else False
    
    elif items[mid] == target:
        return mid
    
    else:
        if items[mid] < target:
            callback_response = binary_search_recur(items[mid:], target)
            int(callback_response)
            return mid + callback_response if callback_response is not False else False
        
        else:
            binary_search_recur(items[:mid], target)
            
    return False
            

print(binary_search_recur(x, target))


# Iterative Implementation of Binary Search Algorithm
def binary_search_iter(items, target):
    start = 0
    end = len(items) - 1
    
    while start < end:
        mid = (start + end) // 2
        
        if items[mid] == target:
            return mid
        
        else:
            if items[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
                
    return False 

print(binary_search_iter(x, target))
# Worried about the little bugs disturbing this algo but I gotta proceed.

# SORTING ALGORITHMS.

# Standard Bubble Sort Algorithm.
def standard_bubble_sort(items):
    
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            
            if items[j] > items[j+1]:
                items[j + 1], items[j] = items[j], items[j + 1]
                
# Modified Bubble Sort Algorithm
def mod_bubble_sort(items):
    
    n = len(items)
    while True:
        swapped = False
        for i in range(1, n):
            if items[i - 1] > items[i]:
                items[i - 1], items[i] =  items[i], items[i - 1]
                swapped = True
        if not swapped:
            break