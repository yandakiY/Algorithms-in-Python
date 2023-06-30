

def fact(n):
    if n == 0:
        return 1;
    
    return n * fact(n-1)

print("Test factoriel de 4 est :" , fact(5))