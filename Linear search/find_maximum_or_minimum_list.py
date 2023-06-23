# Given a list of integers, write an algorithm to find the maximum or minimum of the list. 
# Return the maximum or minimum value found.

# The best way to solve this problem is to sort the lists and get the last and first element of sorted lists.

def find_max_and_min(lists):
    # sorted from smallest to largest
    
    # browse the list in 2 dimensions
    for i in range(len(lists)):
        for x in range(i+1 ,len(lists)):
            if lists[i] > lists[x]:
                [lists[i] , lists[x]] = [lists[x] , lists[i]]
    
    
    # 'Minimum',lists[0])
    # 'Maximum', lists[len(lists)-1]
    return {'min':lists[0] , 'max':lists[len(lists) -1]}


lists_test = [2022 ,2 , 9 , 0 , 11, 102 , 90 , 3 , 2 , 1, 7]

print(find_max_and_min(lists_test))