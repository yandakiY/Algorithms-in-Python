

def bubble_sort(list):
    for i in range(len(list)):
        for x in range(i+1 , len(list)):
            if list[i] >= list[x]:
                list[i] , list[x] = list[x] , list[i]
                
    return list


# Test function
print('Sort ...', bubble_sort([7,44,2,80,17,22]))