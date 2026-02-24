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