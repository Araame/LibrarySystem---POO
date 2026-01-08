nombres = []
nombres_compteur = {}
print("Veuillez donner 7 nombres")
for i in range (1,8):
    nombre = float(input(f"Nombre {i} :"))
    nombres.append(nombre)
    compteur = 0
for i in nombres:
            compteur = compteur + 1
            nombres_compteur[i] = compteur
            print(nombres_compteur)
for doublon,frequence in nombres_compteur.items():
        if(frequence > 1):
            print("Doublons trouvés")
            print(f"Le nombre {doublon} est répété {frequence} fois")
        else:
            print("Aucun doublon")
