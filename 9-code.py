# Manipulation Dictionnaries

# Transforme A list in Dictionnaries

# Listes
listes = [
    'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'
]

# Dictionnaries
dic = {p: listes[p] for p in range(len(listes))}
# Print dictionnarie
# print("Dictionnaries :\n",dic)

# Parcourir chaque items du dictionnaire en affichant l'index et la valeur correspondant a chaque index.
for ind , val in dic.items():
    print("Index:{} Planet:{}".format(ind , val))

