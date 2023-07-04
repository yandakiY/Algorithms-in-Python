# Finding an element in a sorted list :
# Given a sorted list of integers and a target value, 
# write an algorithm to determine whether the target value is present in the list. 
# If so, return the index of the first occurrence, otherwise return -1. 
# Use binary search to improve the algorithm's efficiency.

# function sort list
def sort_list(list):
    # for x in range(len(list)):
    #     for i in range(x+1 , len(list)):
    #         if list[x] >= list[i]:
    #             [list[x] , list[i]] = [list[i] , list[x]]
    # return list
    for i in range(len(list)):
        for x in range(i+1 , len(list)):
            if list[i] >= list[x]:
                [list[i] , list[x]] = [list[x] , list[i]]
    return list

def search_element_list_sorted(list , target , compteur = 0):
    
    # terminal recursion
    if len(list) == 0:
        return -1
    elif list[0] == target:
        return compteur
    else:
        # if list is not empty and the first element is equal to target_element, call function with a increment one of compteur
        return search_element_list_sorted(list[1:] , target , compteur=compteur+1)


def search_element_list_sorted_v1(list , target):
    
    # determine max, min and mid
    # determine start and end
    start = 0
    end = len(list) - 1
    
    while start <= end:
        # mid = (start+end)//2
        mid = (start+end) // 2
        
        if list[mid] == target:
            return mid
        
        if list[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1
    


test_list = sort_list([4,45,55,1,8,55])
print(test_list)
# print('Test search_element_list_sorted({} , 80)'.format(test_list) , search_element_list_sorted(test_list , 80)) # -1
print('Test search_element_list_sorted({} , 45)'.format(test_list) , search_element_list_sorted_v1(test_list , 45)) # 4