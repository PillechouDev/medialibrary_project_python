import document_class

menuEdit = [
    "Titre",
    "Auteur"
]


class AudioDocument(document_class.Document):
    def __init__(self,titre,compositeur,duree,interprete,lien):
        """

        :param titre: Titre de l'audio
        :type titre: str
        :param compositeur: Compositeur de l'audio
        :type compositeur: str
        :param duree: duree en seconde
        :type duree: int
        :param interprete: Interprete de l'audio
        :type interprete: str
        :param lien: Lien de l'audio
        :type lien: str
        """
        document_class.Document.__init__(self,titre,"audio")
        self.compositeur=compositeur
        self.duree =duree
        self.interprete=interprete
        self.lien=lien


    def showAudio(self):
        """

        :return: Print des informations de la musique
        """
        print("Nom du document : " + self.titre + "\nCompositeur : " + self.compositeur + "\nInterprète : " + self.interprete + "\nDurée : " + str(self.duree) + " SEC \n Lien: " + self.lien)

