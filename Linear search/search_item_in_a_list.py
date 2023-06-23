# Given a list of integers and a target value, 
# write an algorithm to determine whether the target value is present in the list. 
# If so, return the index of the first occurrence, otherwise return -1.


def search_item(lists , target_value):
    # check with count(target_value)
    value_present = lists.count(target_value)
    
    # processing when value is in the  lists
    if value_present != 0:
        for i in range(len(lists)):
            if target_value == lists[i]:
                return i
        
    # if(value_present == 0):
    return -1
        
        
# My lists
my_lists = [21 , 110 , 10, 8 ,0 , 21, 3]

print(search_item(my_lists , 0))