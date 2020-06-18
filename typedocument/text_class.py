import document_class


class textDocument(document_class.Document):
    def __init__(self, titre,contenu, auteur):
        document_class.Document.__init__(self,titre)
        self.contenu = contenu
        self.auteur = auteur




