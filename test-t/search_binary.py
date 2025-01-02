
# sorted a list
def sort_list(l: list):
    for x in range(len(l)):
        for i in range(x+1 , len(l)):
            if l[x] > l[i]:
                l[x] , l[i] = l[i] , l[x]
    return l

# 
# find if elem is present
def search_element(l , e):
    # sort this list
    l = sort_list(l)
    print(f'new sort {l}')
    
    # determine start , end
    start = 0
    end = len(l)-1
    # print(len([3]))
    
    # browse each element of l
    while start <= end :
        # define mid
        mid = (start + end) // 2
        
        if e == l[mid]:
            return mid
        
        if e > l[mid]:
            start = mid + 1
        else:
            end = mid - 1
            
    return -1


# find max and min in a list
def find_max_min(l: list):
    # sort this list 
    l = sort_list(l)
    
    # define max , min
    max = l[0]
    min = l[len(l)-1]
    
    # define start and end
    
    start = 0
    end = len(l) - 1
    
    while start <= end:
        # define mid 
        mid = (start+end) // 2
        
        if l[mid] >= max:
            max = l[mid]
        if l[mid] < min:
            min = l[mid]
            
        if max >= l[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return max , min

# find insertion emplacement

def find_emplacement(l:list , e):
    
    # define start , end
    start = 0
    end = len(l) - 1
    
    # sort list
    l = sort_list(l)
    print(f'new sort {l}')
    
    while start <= end:
        
        mid = (start + end) // 2
        
        if l[mid] <= e <= l[mid+1]:
            return mid+1
        
        if l[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    
    # return -1

# Test function
print(search_element([4,22,11,0,3] , 22))
# find max , min
print(find_max_min([4,22,11,0,3]))
# find emplacement
print(find_emplacement([4,22,11,0,3] , 6))

    