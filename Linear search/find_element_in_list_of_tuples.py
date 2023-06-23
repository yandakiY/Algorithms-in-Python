# Finding a specific element in a list of tuples:
# Given a list of tuples where each tuple contains a name and an age, 
# write an algorithm to search the list for a specific name. If the name is found, 
# return the corresponding age, otherwise return -1.

def find_element_in_list_of_tuples(lists_tuples , target_name):
    # print(lists_tuples)
    
    # processing of browse each element
    for i in range(len(lists_tuples)):
        if lists_tuples[i][0] == target_name:
            return i
        
    return -1
    


lists_test = [
    ('Yves' , 20),
    ('Jean' , 18),
    ('Ines' , 48),
    ('Michel' , 32)
]

print('Index of name Yves est :' , find_element_in_list_of_tuples(lists_test , 'Jean-phillipe'))