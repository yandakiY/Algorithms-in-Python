# Calculating the Fibonacci sequence :
# Write a recursive algorithm to calculate the nth term of the Fibonacci sequence. 
# The Fibonacci sequence begins with the numbers 0 and 1, 
# and each subsequent term is the sum of the two preceding terms. For example, 
# if n equals 6, the result must be 8 (because the sequence is 0, 1, 1, 2, 3, 5, 8).

def fibonacci(n):
    
    if n == 0 or n == 1: # terminal recursion
        return n;
    # Formula : Fn = Fn-1 + Fn-2
    return fibonacci(n-1) + fibonacci(n-2)


print("Test fibonacci 6" , fibonacci(6))