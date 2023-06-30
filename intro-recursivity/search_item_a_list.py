# Finding an element in a list:
# Write a recursive algorithm to search for a specific element in a given list. 
# The result must be True if the element is present in the list and False otherwise.

def search_item_in_list(list , e):
    # Explanation
    # Terminal recursion is when list is empty = len(list) = 0
    # if list is empty, False is returned
    # if the first element (list[0]) of the list is equal to the target element we return True
    # otherwise we return the function with a list starting with index 1
    # terminal recursion
    
    if len(list) == 0:
        return False
    elif e == list[0]:
        return True
    else:
        return search_item_in_list(list[1:] , e)
    
    # return True and search_item_in_list(list[1:])
    # pass

print("Search 22 in [4,98,32,22,11]" , search_item_in_list([4,98,32,22,11] , 22)) # True