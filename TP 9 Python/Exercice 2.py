listeA = []
listeB = []
listeC = []
print("Veuillez remplir la liste A ")

#Remplissage de la liste A
for i in range (1,4):
    nombreA = input(f"Valeur {i} :")
    listeA.append(nombreA)
print("Fin de remplissage de la liste A")
#Remplissage de la liste B
for i in range (1,4):
    nombreB = input(f"Valeur {i} :")
    listeB.append(nombreB)
print("Fin de remplissage de la liste B")


print(f"Voici les listes initiales \n Liste A : {listeA} \n Liste B : {listeB}")
listeC = listeA + listeB
print(f"Voici la liste finale \n Liste C : {listeC}")

