import weakref


class Document:
    """
    Classe mère d'un document
    """
    instances=[]
    def __init__(self,titre,type):
        """
        Init de Document
        :param titre: Titre du document
        :param type: Type du document
        """
        self.__class__.instances.append(weakref.proxy(self)) #Ajoute l'object dans la listes d'instances
        self.titre = titre
        self.id = len(self.__class__.instances) #Prend l'id sur la longeurs de instence
        self.type = type

    def getTitre(self):
        """
        :return: Titre du document
        """
        return self.titre

    def editTitle(self):
        """
        :return: Permet de changer le titre d'un document
        """
        print("Choissisez le nouveau titre pour le document : " + self.titre)
        self.titre = input()
        print("Le nouveau nom du document est " + self.titre)




