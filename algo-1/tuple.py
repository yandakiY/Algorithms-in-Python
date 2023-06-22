# Une Lists est une sequence de valeurs.
# Une List peut avoir des elements de differents types.
# En python, l'index commence par 0
# On peut aussi acceder au dernier element par -1
# Avant dernier element -2
# print(planets[1:-1]) // Une List sans le premier et le dernier element
# print(planets[0:3]) // Une list commencant par l'index 0 et terminant a index 3 (Sans l'inclure)
# print(planets[3:]) // Une List commencant par l'index 3 jusqu'a la fin
# -------- Methods Lists ----------
# .append(e) => Ajout de l'element en derniere position
# .pop() => Supprime le dernier element de la liste


primes = [23,3,5,7] 
print("Lists Ordonée", sorted(primes)) # Dans l'ordre croissant

print("Somme des elements", sum(primes)) # 23 + 3 + 5 + 7 = 38

print("Max element",max(primes)) # le plus grand element de la liste est : 38

planets = [
    'Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus', 'Nepturne'
]

planets.append('Pluton') # Lists planets is : ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus', 'Nepturne','Pluton']

# Have the index of Mars
print(planets.index("Mars")) # Index de l'element 'Mars' est : 3



# usage of Tuples
t = (1,2,3)
# Tuple is used for the function who return mutiple values.
# For example a function who give numerator and denominator of a float number

x = 0.125
print(x.as_integer_ratio()) # (1,8)

# test = x.as_integer_ratio();
# print(test[0])
# print()

num , den = x.as_integer_ratio() # Give num for first element of Tuple and den for the second element of Tuple
print(num ,"/", den)