# Algo pour compter le nombre d'occurence present dans une liste
# Les elements de l'array doit etre des nombres generes aleatoirement de 1 a 100
# Utilisation du module random et de la methode .randomint(a , b)
# Resultat : >> numbers_occ([2, 3, 3, 4])
# 2 : 1 occurence
# 3 : 2 occurences
# 4 : 1 occurence

import random

# assignation liste a traité
lists = []

# saisie du nombre du nombre d'element qu'on souhaite
numbers = eval(input("Combien voulez d'element dans la liste :"))

# 1 - Mise en place des valeurs dans la liste
for i in range(numbers):
    # generation aleatoirement du nombre a inserer
    value = random.randint(1 , 100)
    
    # insertion dans lists
    lists.append(value)
# print(len(lists))
print(lists)

# 2 - creer une lists de 100 elements ayant pour valeur pour chaque index 0
lists_occurence = []
for j in range (0 , 101):
    lists_occurence.append(0)
# print(len(lists_occurence))
# print(lists_occurence)
# 3 - parcourir lists par son index

for x in range(len(lists)):
    
    # condition pour voir si lists_occurence est 0
    # si lists_occurence[valeur_de_lists] est 0, si c'est le cas initialisation a 1; sinon on fait +1
    if(lists_occurence[lists[x]] == 0):
        lists_occurence[lists[x]] = 1
    else:
        lists_occurence[lists[x]] += 1
        

# Affichage du resultat
# Affichage des index et des values des elements qui ont des valeurs superieur a 0

for y in range(len(lists_occurence)):
    
    if(lists_occurence[y] > 0):
        print(y , "- occurence :",lists_occurence[y])


# print('Lists occurence',lists_occurence)