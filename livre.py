from document import Document

"""Class Livre
Pour un livre, nous avons : Titre, ID, Auteur, Disponible
"""



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