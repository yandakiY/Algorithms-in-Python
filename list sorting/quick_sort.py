
def quick_sort(list):
    
    if len(list) <= 1:
        return list
    else:
        # define pivot
        pivot = list[0]
        
        # les elements les plus petits de la liste[1:] a etre avant le pivot
        small_elements = [x for x in list[1:] if x <= pivot]
        
        # les elements les plus grands de la liste[1:] a etre apres le pivot
        large_elements = [x for x in list[1:] if x > pivot]
        
        # call recursive function
        return quick_sort(small_elements) + [pivot] + quick_sort(large_elements)
    

print('List to treat', [4 , 7 , 2, 80 , 17 , 22])
# Test function
print('Sorted...', quick_sort([4 , 7 , 2, 80 , 17 , 22]))