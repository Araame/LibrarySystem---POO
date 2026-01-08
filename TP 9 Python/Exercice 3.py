nombres = []
positifs = []
print("Veuillez donner 10 nombres psitifs ou négatifs")
for i in range (1,11):
    nombre = float(input(f"Nombre {i} :"))
    nombres.append(nombre)
for i in nombres :
    if (i >= 0):
        positifs.append(i)

print("Voici les nombres qui sont positifs")
print(positifs)

