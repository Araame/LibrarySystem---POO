from document import Document
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