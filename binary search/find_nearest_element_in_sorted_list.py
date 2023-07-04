# Finding the nearest element in a sorted list :
# Given a sorted list of integers and a target value,
# write an algorithm to find the element closest to the target value in the list. 
# Use binary search to improve the algorithm's efficiency.

# sort list
def sort_list(list):
    for x in range(len(list)):
        for i in range(x+1 , len(list)):
            if list[x] >= list[i]:
                list[x] , list[i] = list[i] , list[x]
                
    return list

# main function
def find_nearest_element(list , target_value):
    list = sort_list(list)
    
    # define start and end
    start = 0
    end = len(list)-1
    
    # define near_element
    near_element = None
    
    while start <= end:
        # define mid = (start + end) // 2
        mid = (start + end) // 2
        
        if list[mid] == target_value:
            return list[mid]
        
        if list[mid] < target_value:
            start = mid + 1
        else:
            end = mid - 1
        
        # change near_element
        if near_element is None or abs(list[mid] - target_value) < abs(near_element - target_value):
            near_element = list[mid]
            
    return near_element


ex_list = [3,9,2,10]
print('Test' , find_nearest_element(ex_list , 7))