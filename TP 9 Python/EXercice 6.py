mots = []
liste_voyelles = ['a','e','i','o','u','y']
dict_mots = {}
for i in range(1,5):
    mot_entre = input(f"Mot {i} :")
    mots.append(mot_entre.lower())
for mot in mots:
    nombre_voyelles = 0
    for i in mot :
        if (i in liste_voyelles):
            nombre_voyelles = nombre_voyelles + 1
        dict_mots [mot] = nombre_voyelles

print(dict_mots)

