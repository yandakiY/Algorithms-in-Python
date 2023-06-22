# Algo de tri de list 
# Tri du plus petit au plus grand (Ordre croissant)
# utilisation boucle for x in range(...)

# Saisie du nombre d'element souhaité
# Saisie des elements 
# Tri
# Affichage

# Request
number_element = eval(input("How many element would like you ?"))

# My lists
lists = []

# Operation de saisie
for i in range(number_element):
    element = eval(input("Element {} : ".format(i+1)))
    lists.append(element)
    
# print(lists)

for x in range(len(lists)):
    print(lists[x])
    # Another loop for comparaison
    for y in range(x+1 , len(lists)):
        if lists[x] >= lists[y]:
            [lists[x] , lists[y]] = [lists[y] , lists[x]]
            

print("Result : ", lists)