import document_class

menuEdit = [
    "Titre",
    "Auteur",
    "Content"
]


class textDocument(document_class.Document):
    """
        Classe de d'un document texte
    """
    def __init__(self, titre, auteur, contenu):
        document_class.Document.__init__(self, titre)
        self.content = contenu
        self.author = auteur

    def showTextDocument(self):
        print("Titre : " + self.titre + "\n Autheur : " + self.author + "\n Contenu : " + self.content)

    def menuEditTextDocument(self):
        try:
            print("Voulez-vouz vraiment editer " + self.titre + "? (Oui = 1 Non=2 )")
            response = int(input())
            if response == 1:
                print("Qu'est ce que vous voulez éditer ? \n")
                count = 1
                for menu in menuEdit:
                    print((str(count) +". "+ menu.title()))
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
        print("Veuillez entrez le nouveau nom de l'auteur pour le document '"+self.titre + "' (Ancien auteur : "+ self.author + ")")
        self.author=input()
        print("Le nouveau auteur est " +self.author +" pour le doccuement : " + self.titre)