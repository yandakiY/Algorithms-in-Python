# Searching for a word in a list of strings :
# Given a list of strings, write an algorithm to search the list for a specific word. 
# If the word is found, return the index of the string in the list, otherwise return -1.


def search_a_word_in_list(lists , target_value):
    
    # browse each element of lists
    # compare each elemet with the target_value
    
    # check count
    count_target = lists.count(target_value)
    
    if count_target == 0 :
        return -1

    for i in range(len(lists)):
        if lists[i] == target_value:
            return i



lists_test = ['Boa','Yandaki','Yves','Michel','Marie','Grace','Maeva']

print('Index of Yves', search_a_word_in_list(lists_test , 'Michel'))