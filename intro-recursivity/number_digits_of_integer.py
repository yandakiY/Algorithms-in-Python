# Calculating the number of digits in an integer :
# Write a recursive algorithm to count the number of digits in a given integer. 
# For example, if the integer is 1589, the result must be 4.

# uniquement quand le parametre est string
def number_digit_interger_v1(n): 
    # print(len(str(n)))
    
    # determine terminal recursion
    if len(n) == 0: 
        return 0
    
    # divide 
    return len(n) + number_digit_interger_v1(n.split()[1:])
    
    

def number_digit_interger_v2(n):
    
    # check if the number is less than 10: 
    # if so, return 1.
    # if not divide recursively the number by 10 and increment (+1)
    
    # terminal recursion
    if n < 10:
        return 1
    else:
        return 1 + number_digit_interger_v2(n // 10) 

print('Number digit', number_digit_interger_v1('13450004'))
print('Number digit with v2', number_digit_interger_v2(13450004))