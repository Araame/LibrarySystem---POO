from livre import Livre
from magazine import Magazine
from adherent import Adherent





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







