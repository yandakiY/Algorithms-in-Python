# Calculating the sum of elements in a list :
# Write a recursive algorithm to calculate the sum of the elements in a given list. 
# For example, if the list is [2, 4, 6, 8], the result should be 2 + 4 + 6 + 8 = 20.

def sum_list_element(list):
    
    if len(list) == 0: # terminal recursion
        return 0
    
    return list[0] + sum_list_element(list[1:])


print('test [4 , 5 , 43 , 10]' , sum_list_element([4 , 5 , 43 , 10])) # 53 + 9 = 62