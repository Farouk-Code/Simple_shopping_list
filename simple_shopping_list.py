import sys

liste = []
ajouter = "1"
retirer = "2"
afficher = "3"
vider = "4"
quitter = "5"
choix = ""

while choix != quitter:
    choix = input("Choisissez parmi les 5 options suivantes :\n1: Ajouter un élément à la liste\n2: Retirer un élément à la liste\n3: Afficher la liste\n4: Vider la liste\n5: Quitter\n 👉 Votre choix : ")
   
    #01 : Ajouter un élément
    if choix == ajouter:
        element = input("\nQue voulez-vous ajouter ?\n")
        liste.append(element)
        print(f"{element} a été ajouté à la liste\n")
    
    #02 : Supprimer un élément
    elif choix == retirer:
        element = input("\nQue voulez-vous retirer ?\n")
        #Vérifier si l'élément existe dans le liste
        if element in liste:
            liste.remove(element)
            print(f"{element} a été retiré de la liste !\n")
        else:
            print("\nCet élément n'existe pas !\n")
    
    #03 : Afficher la liste
    elif choix == afficher:
        taille_liste = len(liste)
        rang = 0
        #Vérifier si il existe des éléments dans la liste'
        if taille_liste == 0:
            print("\nLa liste est vide.\n")
        else:
            print(f"\nVotre liste est composé de {taille_liste} éléments : ")
            for i in liste:
                rang += 1
                #Vérifier si c'est le dernier élément de la liste
                if rang == taille_liste:
                    print(f"{rang}. {i}\n")
                else:
                    print(f"{rang}. {i}")
   
    #04 : Supprimer le contenu de la liste
    elif choix == vider:
        if len(liste) > 0:
            liste.clear()
            print("\nVotre liste a été vidé.\n")
        else:
            print("\nLa liste est vide.")
   
    #Quitter le programme
    elif choix == quitter:
        print("\nAu revoir !")
        sys.exit()   
    else:
        print(f"\n{choix} n'est pas une option.\n")

         