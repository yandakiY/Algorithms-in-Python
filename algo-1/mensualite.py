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

# Calcul taux mensuel
# Attention a la division d'un pourcentage: diviser le taux par 100 avant de faire autres operations
T = (Ta / 100) / 12
print("Taux mensuel :", T)

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

print("Mensualité :",M)