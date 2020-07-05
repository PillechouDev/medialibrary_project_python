import document_class

menuEdit = [
    "Titre",
    "Auteur"
]


class ImageDocument(document_class.Document):
    """
    Classe d'une image
    """

    def __init__(self, titre, art, auteur, lien):
        """
        :param titre: Titre du document
        :param art: Ascii art de l'image
        :param auteur: Auteur de l'image
        :param lien: Lien de l'iamge
        """

        document_class.Document.__init__(self, titre,"image")
        self.ascii = art
        self.auteur = auteur
        self.lien = lien

    def showImage(self):
        """
        :return: print du contenu de l'image
        """
        print("Nom du document : " + self.titre + "\nAuteur : " + self.auteur + "\nLien : " + self.lien + "\nAscii : " + self.ascii)

    def menuEditTextDocument(self):
        """
        :return: Menu d'edit du document
        """
        try:
            print("Voulez-vouz vraiment editer " + self.titre + "? (Oui = 1 Non=2 )")
            response = int(input())
            if response == 1:
                print("Qu'est ce que vous voulez éditer ? \n")
                count = 1
                for menu in menuEdit:
                    print((str(count) + ". " + menu.title()))
                    count += 1
                response = int(input())
                if response == 1:
                    self.editTitle()
                elif response == 2:
                    self.editAuthor()
                else:
                    self.errorValue()

            elif response == 2:
                return 0
            else:
                self.errorValue()
        except ValueError:
            self.errorValue()

    def errorValue(self):
        print("Mauvaise valeurs ! Retour au menu")
        self.menuEditTextDocument()

    def editAuthor(self):
        print(
            "Veuillez entrez le nouveau nom de l'auteur pour le document '" + self.titre + "' (Ancien auteur : " + self.author + ")")
        self.author = input()
        print("Le nouveau auteur est " + self.author + " pour le doccuement : " + self.titre)
