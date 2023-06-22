# Check if a number is Prime or not


# Implementation de la fonction
def check_prime(n):
    # isPrime = False
    iteration = 0
    for e in range(2 , n-1):
        # count of iteration
        iteration += 1
        # check if the number is divisible by 0 (number % e == 0)
        if (n % e == 0):
            print('Iteration effectué : ',iteration)
            return False
    
    print('Iteration effectué : ',iteration)
    return True

print(check_prime(29))
# number = eval(input("Numbre :"))

