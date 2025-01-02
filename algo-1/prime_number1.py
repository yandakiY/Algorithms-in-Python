import math
# Check if a number is Prime or not


# Implementation de la fonction
def check_prime(n):
    isPrime = True
    iteration = 0
    # check if number is not 2
    # if number is 2 == True
    if(n != 2):
        
        # check if number who is different of 2 is peer.
        if(n % 2 == 0):
            isPrime = False
            iteration = 1
        else:
            # Determiner la limite (racine(n)+1)
            limite = int(math.sqrt(n) + 1)
            
            # verifier les diviseurs impairs
            for e in range(3,limite,2):
                # Compter le nombre d'iterations a faire
                iteration += 1
                if(n % e == 0):
                    isPrime = False
        # return isPrime
    
    print("Iteration :",iteration)
    return isPrime

print(check_prime(37))
# number = eval(input("Numbre :"))

