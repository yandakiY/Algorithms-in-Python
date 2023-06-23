# Finding the frequency of an element in a list :
# Given a list of integers and a target value, 
# write an algorithm to determine how often the target value appears in the list. 
# Return the number of times the target value occurs.


def find_frequency_element(lists , target_value):
    # scroll list items
    
    frequency = 0
    
    # browse each element in lists for the comparaison
    for i in range(len(lists)):
        if lists[i] == target_value:
            frequency += 1
    
    return frequency


lists_test = [1 , 20 , 0.0 , 3 , 5 , 22 , 45 , 0 , 0 , 20 ,11]

print('Frequency of 0 :' , find_frequency_element(lists_test , 0))