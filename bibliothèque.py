
"""Class Livre
Pour un livre, nous avons : Titre, ID, Auteur, Disponible
"""
from abc import ABC, abstractmethod

class Document (ABC): 
    """Classe générique : document """
    def __init__ (self, titre, auteur, disponibilite):
        self.titre = titre
        self.auteur= auteur
        self.__disponibilite = disponibilite

    @abstractmethod
    def get_disponibilite(self):
        pass
    
    @abstractmethod
    def set_disponibilite(self):
        pass    



class Livre(Document):
    """Classe livre qui hérite de document car un livre est un type de document"""
    def __init__(self, titre, auteur, disponibilite=True):
        super().__init__(titre, auteur, disponibilite)
        self.__disponibilite = disponibilite
        
    
    def __str__(self):
        if self.__disponibilite:
            return f"{self.titre} : { self.auteur} | { self.__disponibilite}"
    
    def get_disponibilite(self):
        return self.__disponibilite


    def set_disponibilite(self):
        if self.__disponibilite == True:
           self.__disponibilite = False
        else:
            self.__disponibilite = True
            return  self.__disponibilite


   

class Magazine(Document):
    """Classe magazine qui hérite de document car un livre est un type de document"""
    def __init__(self, titre, auteur, frequence, disponibilite = True, type_doc = "Magazine"):
        super().__init__(titre, auteur, disponibilite)
        self.frequence = frequence 
        self.__disponibilite = disponibilite
        self.type_doc = type_doc

        
         
    def __str__(self):
        return f"{self.titre} : { self.auteur} | { self.__disponibilite} {self.frequence}"
    
    
    def get_disponibilite(self):
        return self.__disponibilite


    def set_disponibilite(self):
        if self.__disponibilite == True:
           self.__disponibilite = False
        else:
            self.__disponibilite = True
            return  self.__disponibilite

        


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

        




""" Class Bibliothécaire
""" 
class Manager:
    def __init__(self):
      self.liste_livre = []
      self.liste_adherent = []
      
    def ajouter_livre(self, titre, auteur):
        ajout = Livre(titre, auteur)
        self.liste_livre.append(ajout)
        print(f"Livre '{titre}' ajouté avec succès !")
        
    def ajouter_mangazine(self, titre, auteur, frequence):
        ajout = Magazine(titre, auteur, frequence)
        self.liste_livre.append(ajout)
        print(f"Votre magazine est ajoutée avec succès")

   

    
    def inscription(self, id, nom):
        inscrit = Adherent(id, nom)
        self.liste_adherent.append(inscrit)
        print("Adhérent inscrit")



    def valider_emprunt(self, titre, nom):
            for titre in self.liste_livre:
                if titre.lower() in self.liste_livre :
                        print("Livre trouvé")
                        position_livre = self.liste_livre.index(titre)
                        
                        if self.liste_livre[position_livre].get_disponibilite():
                            print("Livre disponible")
                        for adherent in self.liste_adherent :
                                if  nom.lower() in adherent.nom :
                                    print("Adhérent trouvé")
                                    adherent.liste_emprunt.append(titre)
                                    print("Emprunt validé")
                                    self.liste_livre[position_livre].set_disponibilite()


                                else:
                                    print("Adhérent inexistant")

                else:
                    print("Livre introuvable")
            
        
    def enregistrer_un_retour(self, titre, nom):
            for adherent in self.liste_adherent:
                if  nom in  adherent.nom:
                    print ("print adherent trouvée")
                else:
                    print("Ce nom n'existe pas ")
                for livre in self.liste_livre:
                    if titre in livre.titre:
                        print("livre touvé") 
                        livre.set_disponibilite()
                        adherent.liste_emprunt.pop(titre)
                        print("Livre restitué")

                    else :
                        print ("ce livre n'existe pas")




""" Class Interface
"""

class Menu:
    def __init__(self):
      self.manager = Manager()

    def lancer_menu(self):
        while True:
            print("\n Dalal Ak Jamm Çi Sama biblio")
            print("1. Ajouter un livre")
            print("2. Ajouter un magazine")
            print("3. Inscrire un adhérent")
            print("4. Valider un emprunt")
            print("5. Enregistrer un retour")
            print("6. Liste des livres")
            print("7. Liste des adhérents")
            print("8. Liste des livres")
            print("9. Quitter")

            choix = input("Veuillez entrer le nombre de votre choix: ")
    
            match choix:
                case "1":
                    while True:
                        titre = input("Titre: ").capitalize()
                        if titre.isalpha():
                            break
                        else:
                            print("Titre invalide (3 caractères minimums)")
                    
                    while True:
                        auteur = input("Auteur: ").capitalize()
                        if auteur.isalpha():
                            break
                        else:
                            print("Nom invalide !")
                            
                    self.manager.ajouter_livre(titre, auteur)

                case "2":

                    while True:
                        titre = input("Titre: ").capitalize()
                        if titre.isalpha():
                            break
                        else:
                            print("Titre invalide (3 caractères minimums)")
                    
                    while True:
                        auteur = input("Auteur: ")
                        if len(auteur) >=3:
                            break
                        else:
                            print("Nom invalide !")
                    
                    while True:
                        frequence = input ("Frequence : ").lower()
                        
                        if frequence not in ["hebdomadaire", "journalier", "mensuelle"]:
                            print(f"La fréquence est incorrecte")
                        else:
                            break
                            
                    self.manager.ajouter_mangazine(titre, auteur,frequence)


                case "3":
                    while True:
                        id = input("ID: ")
                        if id is not None:
                            break
                        else:
                            print("L'identifiant ne doit pas être nul")
                    while True:
                        nom = input("Nom: ").strip().capitalize()
                        if len(nom) >= 2:
                            self.manager.inscription(id, nom)
                            break

                case "4":
                    t_livre = input("Titre du livre: ")
                    n_adh = input("Nom de l'adhérent: ")
                    self.manager.valider_emprunt(t_livre,n_adh)

                case "5":
                        nom_ad= input ("entrer le nom: ")
                        titre_lv = input ("entrer le titre du livre")
                        self.manager.enregistrer_un_retour(titre_lv, nom_ad)

                case "6":
                    print("--- Liste des livres ---")
                    for i, liste in enumerate(self.manager.liste_livre, 1):
                        print(f"{i}: {liste}")
                
                case "7":
                    print("--- Liste des adhérents ---")
                    for i, liste in enumerate(self.manager.liste_adherent, 1):
                        print(f"{i}: {liste}")

                case "8":
                    print("--- Liste des magazines ---")
                    for i, liste in enumerate(self.manager.liste_livre, 1):
                        if liste.type_doc == "Magazine":
                            print(f"{i}: {liste}")
                
                case "9":
                    print("Au revoir!")
                    break


if __name__ == "__main__":
   menu= Menu()
   menu.lancer_menu()