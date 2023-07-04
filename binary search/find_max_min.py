# For the result of this algo, we need to define start , end and mid
# start eq to 0
# end eq to the length of list substract to one
# mid eq to start+end // 2


# writing sort function
def sort_list(list):
    for i in range(len(list)):
        for x in range(i+1 , len(list)):
            if list[i] >= list[x]:
                [list[i] , list[x]] = [list[x] , list[i]]
    return list

# if list is sort
def find_max_min(list):
    
    list = sort_list(list)
    
    start = 0
    end = len(list) - 1
    
    
    # define max and min 
    max = list[start]
    min = list[start]
    
    while start <= end:
        
        # determine mid 
        mid = (start+end) // 2
        
        if list[mid] > max:
            max = list[mid]
        
        if list[mid] < min:
            min = list[mid]
            
        if list[mid] <= max:
            start = mid + 1
        else:
            end = mid - 1
        
    return max , min


# if list is not sort
def find_max_min_v1(list):
    # define max and min
    max = list[0]
    min = list[0]
    
    # browse each element of list
    for e in list:
        if e > max:
            max = e
        if e < min:
            min = e
    
    return max , min


print('Test' , find_max_min([3,33,4,4,10,2]))
print('Test' , find_max_min_v1([1,3,33,4,4,10,2,44]))
            
        