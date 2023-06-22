# Le but de cet algo est de determiner le nombre d'occurences pour une valeur.
# Par exemple pour une lists : [3,2,6,5,3,9,2]
# On aura : 
# 3 : 2 occurences
# 2 : 2 occurences
# 6 : 1 occurence
# 5 : 1 occurence
# 9 : 1 occurence
import random

# Notre lists a gerer
lists = []

size_lists = eval(input("Taille de la listes"))

for i in range(size_lists):
    # Assignation de valeur generé aleatoirement de 1 a 100
    value = random.randint(1 , 100)
    
    # Ajout de la valeur dans la lists
    lists.append(value)

# print("Length :", len(lists))

print("Liste",lists)
# Trouver le nombre d'occurence pour chaque valeur de la lists
for i in range(len(lists)):
    
    # par defaut le nombre a pas deja été trouvé ou traité
    finded = False

    # verifier l'indice i par rapport aux element avant lui  
    for j in range(i):
        if (lists[i] == lists[j]):
            finded = True
    
    # Operation si l'element est deja present a gauche
    if (finded == False): # element pas present a gauche
        # occurence = 1
        occurence = 1
        
        # parcours la liste vers la droite
        for x in range(i+1 , len(lists)):
            if (lists[i] == lists[x]):
                occurence = occurence + 1
        
        # Apres avoir verifier si l'element n'a pas encore été parcouru et d'avoir compté le nombre d'occurence
        # Affichage du nombre d'occurence
        print(lists[i]," :",occurence," occurence") 
    

# print(lists)