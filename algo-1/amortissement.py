# Calcul de la mensualité par mois
# On a besoin du capital (C), du nombre d'années et du nombre de mois (A, N = A*12)
# On a besoin du taux annuel (Ta) et du taux mensuel (T = Ta/12)
# Formule : M = C*T * ((1+T)**N ) / ((1+T)**N - 1)

# Assignation Capital
C = eval(input("Votre capital :"))
# print("Capital :", C)

# Assignation Nombre d'année et nombre de mois
A = eval(input("Nombre d'année(s):"))
# print("Année :", A)

# determination nombre de mois
N = A * 12
# print("Nombre de mois :", N)

# Assignation Taux annnuel et mensuel
Ta = eval(input("Votre taux annuel (en %) :"))
# print("Taux annuel :", Ta)

# Calcul taux mensuel (T)
# Attention a la division d'un pourcentage: diviser le taux par 100 avant de faire autres operations
T = (Ta / 100) / 12
print("Taux mensuel :", T)


# Assignation du taux de l'assurance
Tass = eval(input("Taux d'assurance (en %) :"))
# print("Taux d'assurance ",Tass)

# Calcul de la second partie de la formule ((1+T)**N / (1+T)**N - 1)
# calcul du numerateur : (1+T)**N
num = (1+T)**N

# calcul du denominateur
den = num - 1

# second_part
second_part = num/den

# calcul de la premiere partie de la formule C*T
first_part = C*T

# Calcul final : M = first_part * second_part
M = first_part*second_part

# Calcul Mensualité sans le cout de l'assurance
print("Mensualité sans assurance :",round(M))

# Avec cout de l'assurance (MAA) : M + cout_assurance
cout_assurance = C * ((Tass/100)/12)
print("Cout de l'assurance", round(cout_assurance))
# calcul MAA
MAA = M + cout_assurance
print("Mensualité avec assurance :",round(MAA))

# Process d'amortissement
cap_restant = C
print("Mensualite", "Amortissement","Interets","Capital","Ass.", end=' ')
print('\n')

# i = 0
for i in range(N):
    # i += 1
    calcul1 = cap_restant*T
    calcul2 = (1+T)**(N-i)
    
    calcul3 = calcul2-1
    
    M = calcul1 * (calcul2/calcul3)
    MAA = M+cout_assurance
    
    interets = calcul1
    amort = M-interets
    
    cap_restant -= amort
    
    print(round(M) , round(amort) ,round(interets) , round(cap_restant) , round(cout_assurance))