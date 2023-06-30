

def puissance(x , n):
    
    if n == 0:
        return 1;
    elif n < 0:
        return 1 / puissance(x , -n)
    elif n % 2 == 0:
        temp = puissance(x , n//2)
        return temp*temp
    else:
        return x * puissance(x , n-1)
    
    
print(puissance(4,-1))