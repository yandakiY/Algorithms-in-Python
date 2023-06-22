# Tuple manipulation
# 
tuple_1 = (1 , 2 ,3 , 34 ,5 ,100)
tuple_2 = (6 , 8 , 9)

# Syntaxe : tuple[indexDebut:indexFinNonInclus]
print(tuple_1[1:2]) # Affichage : (2,)
print(tuple_1[2:5]) # Affichage : (3,34,5)

for i in range(len(tuple_1)):
    print(tuple_1[i])

# Concatenation
# concatenation = tuple_1 + tuple_2

# print("Concatenation : ",concatenation)