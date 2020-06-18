from typedocument.text_class import textDocument
from document_class import Document


test = textDocument("Pioupiou", "Pioupiou est mort ce soir", "MoiLol")

print(test.getTitre())


test.editTitle("Gégé")