""" Class Adhérent
Pour un adhérent nous avons son nom, son id et la liste de ses emprunts 
""" 
class Adherent:

    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        self.liste_emprunt = []
    def __str__(self):
        return f"{self.id} : {self.nom} "