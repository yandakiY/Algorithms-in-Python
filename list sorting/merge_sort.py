
# define merge sort

def merge_sort(list):
    
    if len(list) <= 1:
        return list
    else:
        # define start and end
        
        # define mid
        mid = len(list) // 2
        
        # part left
        part_left = list[:mid]
        
        # part right
        part_right = list[mid:]
        
        # half
        part_left = merge_sort(part_left)
        part_right = merge_sort(part_right)
        
        list_return = fusion(part_left , part_right)
        
        return list_return

# define fusion function

def fusion(list_left , list_right):
    
    list_sort = []
    i = 0 # For list left
    j = 0 # For list right
    
    while i < len(list_left) and j < len(list_right):
        
        # check if element of list_right is large than element of list_left, append list_left element 
        if list_left[i] <= list_right[j]:
            list_sort.append(list_left[i])
            # increment i
            i += 1
        else:
            list_sort.append(list_right[j])
            j += 1
        
    # fusionner avec .extend()
    # extend left part
    list_sort.extend(list_left[i:])
    # extend right part
    list_sort.extend(list_right[j:])
    
    return list_sort


# Test fusion function
# print('Fusion ...', fusion([1,4] , [8,11]))

trie_list = merge_sort([4,90,2,39,1])
print("Test sort [4,90,2,39,1] =>" , trie_list)