# Definir une fonction qui determine si un nombre est premier ou non
# Demander un intervalle commencant par 0 et donner les nombres premiers qui sont dans cet intervalle
# Decomposer un nombre (prealablement saisie) a partir des nombres premiers trouvés dans l'intervalle
import math

def is_prime(n):
    
    # determiner si le nombre est 2 (dans ce cas 'nombre premier')
    # determiner si le nombre est pair
    # determiner la racine carrée du nombre saisie
    # verifier si les nombres impairs de 0 a racine + 1 sont divisible
    
    isPrime = True
    
   
    if (n == 2):
        return isPrime
    elif (n % 2 == 0):
        isPrime = False
    else:
        # determiner le racine carrée
        last_divisible = int(math.sqrt(n) + 1)
        
        for i in range(3,last_divisible,2):
            if (n % i == 0):
                isPrime = False
    
    return isPrime

# assignation du nombre a traité
number = eval(input("Nombre a decomposer :"));

# initialisation de la liste contenant les nombres premiers
list_primes = []

for i in range(1,number+1):
    
    # verifier si i est un nombre premier
    # utlisation de is_prime
    
    if(is_prime(i)):
        list_primes.append(i)

print("Liste des nombres premiers", list_primes)

# traitement

# valeur a retourné
lists_diviseurs = []

# traitement...
copy_number = number
for x in range(0 , len(list_primes)):
    
    
    # verification, si value est divisible par list_primes[x]
    if(number % list_primes[x] == 0):
        # insertion du nombre premier divisible 
        lists_diviseurs.append(list_primes[x])
        
        # mise a jour de 'number'
        number = number / list_primes[x]
    
    # add number in lists of diviseurs 
    if(number <= list_primes[x+1] and number != 1):
        lists_diviseurs.append(int(number))
        break


# print
print("Resultat de la decomposition ", copy_number , ":" , lists_diviseurs)
