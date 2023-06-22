# import numpy as np

# def d'une fonction qui calcul la moyenne des elements d'une lists

def avg_lists(lists):
    # determine length
    length_litst = len(lists)
    
    # determine sum of lists
    sum_lists = sum(lists)
    
    return sum_lists / length_litst

# Test algorithme avec le langage python

# inserer un nombre precis d'elements selon un nombre donné

# nombre = eval(input("Nombre de notes : "))

# Assignation de la listes sans taille 
lists_notes = []

# 1 - Assignation des notes en fonction du nombre de note
# for i in range(0 ,nombre):
#     note = eval(input("Note :"))
#     lists_notes.append(note)

# 2 - utilisation de la boucle while (condition):
# Pas de prise en compte du nombre de notes
# Arret de l'insertion de note quand une valeur negative est saisie

note = 0
nb_notes = 0
while (note >= 0):
    # Saisie de la note
    note = eval(input("Note :"))
    
    # check note is positive or negative
    if(note < 0):
        nb_notes -= 1
        break
    
    # Mise a jour du compteur (nb_notes)
    nb_notes += 1
    
    # Ajout de la note a la liste
    lists_notes.append(note)
    
    
        
        
print("Notes ",lists_notes)
print("Moyenne :", avg_lists(lists_notes))