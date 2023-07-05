

def insert_sorting(list):
    
    # define n
    n = len(list)
    
    # Browse each element of list
    for i in range(1 , n):
        current_value = list[i]
        # define j : the first previous element
        j = i - 1
        # Compares current value with previous elements
        # If the current value is lower than one of the previous elements, we exchange it.
        while j >= 0 and list[j] > current_value:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = current_value
        
    return list
        

# Test
print('Sort...' , insert_sorting([4,90,2,39,1]))