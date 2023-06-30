# Calculating the sum of numbers up to N :
# Write a recursive algorithm to calculate the sum of numbers from 1 up to a given number N. 
# For example, if N equals 5, the result should be 1 + 2 + 3 + 4 + 5 = 15.

def sum_number_to_N(n):
    
    if n == 0: # terminal recursion
        return 0
    
    return n + sum_number_to_N(n-1)

print('Test 10' , sum_number_to_N(10))