


class Document:
    def __init__(self,titre):
        self.titre = titre


    def getTitre(self):
        return self.titre

    def editTitle(self):
        print("Choissisez le nouveau titre pour le document : " + self.titre)
        self.titre = input()
        print("Le nouveau nom du document est " + self.titre)