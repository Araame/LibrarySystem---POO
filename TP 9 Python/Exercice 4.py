nombres = []
pairs = []
impairs = []

print("Veuillez donner 8 nombres")
for i in range (1,9):
    nombre = int(input(f"Nombre {i} :"))
    nombres.append(nombre)
for i in nombres :
    if (i %2 == 0):
        pairs.append(i)
    else:
        impairs.append(i)

print(f"Voici la liste initiale \n Liste : {nombres} \n Voici les nombres pairs : {pairs} \n Voici les nombres impairs : {impairs}")


