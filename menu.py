from bibliothèque import Manager

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