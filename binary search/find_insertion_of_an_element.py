# Finding the insertion of an element in a sorted list :
# Given a sorted list of integers and a target value, 
# write an algorithm to find the index where the target value should be inserted into the list so as to preserve the sort order. 
# Use binary search to improve the algorithm's efficiency.


# function sort a list
def sort_list(list):
    for e in range(len(list)):
        for x in range(e+1 , len(list)):
            if list[e] > list[x]:
                list[e] , list[x] = list[x] , list[e]
    
    return list


def find_index_element(list , target_value):
    
    list = sort_list(list)
    print('List to sorted', list)
    
    # define start and end
    start = 0
    end = len(list) - 1
    
    # check if target_value is greater than the last element of sorted list
    # if target_value is greater than the last element of sorted list return last index
    
    if target_value > list[len(list) - 1]:
        return len(list)
    
    # If target value is less than the first element, return 0
    if target_value < list[0]:
        return 0
    
    while start <= end:
        # define mid
        mid = (start + end) // 2
        
        if list[mid] <= target_value and list[mid+1] >= target_value:
            return mid+1
        
        if list[mid] < target_value:
            start = mid + 1
        else:
            end = mid - 1
    

# Test function
ex_type = [3 , 5 , 10 , 2]
print('Insert {} to index'.format(7),find_index_element(ex_type , 7))