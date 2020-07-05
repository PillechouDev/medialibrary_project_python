from typedocument.audio_class import AudioDocument
from typedocument.image_class import ImageDocument
from typedocument.text_class import textDocument


art =str("""""""""-.
           '       
          |,.  ,-.  |
          |()L( ()| |
          |,'  `".| |
          |.___.',| `
         .j `--"' `  `.
        / '        '   
       / /          `   `.
      / /            `    .
     / /              l   |
    . ,               |   |
    ,"`.             .|   |
 _.'   ``.   o     | `..-'l
|       `.`,        |      `.
|         `.    __.j         )
|__        |--""___|      ,-'
   `"--...,+""""   `._,.-' mh)""")


from document_class import Document

text1= textDocument('La cigale et la fourmi',"Jean De la fontaine","La Cigale, ayant chanté \nTout l'été,\nSe trouva fort dépourvue\nQuand la bise fut venue :\nPas un seul petit morceau\n")
image1= ImageDocument('Tux',art,"Linus Torvalds","https://fr.wikipedia.org/wiki/Tux#/media/Fichier:Tux.svg")
audio1= AudioDocument('Valse n°2','Dimitri Chostakovitch',233,'Orchestre Universitaire de Lille','https://www.youtube.com/watch?v=tv8nF49alQk')

continu =True


print("Bienvenue dans la médiathèque devloppée par Yohan Widogue")
while continu == True:
    print("Que voulez vous faire ? \n 1.Consulter un document \n2.Nouveau document\n3.Quitter")
    try:
        choix = int(input())

        if choix == 1:
            print("Voici les documents actuelement stocké: ")
            for object in Document.instances:
                print(str(object.id) + " : "+object.titre + "(Type : "+ object.__class__.__name__+")")
            print("Quel document voulez vous consulter ? ")
            choix = int(input())
            for object in Document.instances:
                if object.id==choix:
                    if object.type == "audio":
                       object.showAudio()
                    elif object.type =="text":
                        object.showTextDocument()
                    elif object.type =="image":
                        object.showImage()
        elif choix == 2:
            print("Quel type de document voulez vous crée ?\n1.Audio\n2.Text\n3.Image")
            choix = int(input())
            if choix == 1:
                newdocAudio=AudioDocument(input("Veuillez saisir le titre : "),input("Veuillez saisir le Compositeur : "),int(input("Veuillez saisir la durée : ")),input("Veuillez saisir l'interprète : "),input("Veuillez saisir le lien : "))
            elif choix ==2:
                newdocText=textDocument(input("Veuillez saisir le titre : "),input("Veuillez saisir l'auteur : "),input("Veuillez saisir le contenu: "))
            elif choix ==3:
                newdocImage=ImageDocument(input("Veuillez saisir le titre : "),input("Veuillez entrez l'ascii art : "),input("Veuillez saisir l'auteur' : "),input("Veuillez saisir le lien : "))

        elif choix == 3:
            continu=False

    except ValueError:
        print("Mauvais choix, recommencer")
        pass