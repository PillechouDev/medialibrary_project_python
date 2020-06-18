


class Document:
    def __init__(self,titre):
        self.titre = titre


    def getTitre(self):
        return self.titre

    def editTitle(self, titre):
        self.titre = titre
        print("Le nouveau nom du document est " + self.titre)