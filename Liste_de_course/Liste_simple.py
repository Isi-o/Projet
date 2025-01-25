import sys

course = [ ]
choix = """Choisissez parmis ces 5 options :
1 : ajouter un élément à la liste
2 : retirer un élément de la liste
3 : afficher la liste
4 : vider la liste
5 : quitter
Votre choix : """
choix_menu = ["1", "2", "3", "4", "5"]

while True:
    choix_utilisateur = input(choix)
    if choix_utilisateur not in choix_menu:
        print("Veuillez effectuer un choix valide.")
        continue

    if choix_utilisateur == "1":
        élément = input("Choisir un élément à ajouter à la liste : ")
        course.append(élément)
        print(f"{élément} a bien été ajouté à votre liste.")

    elif choix_utilisateur == "2":
        élément = input("Choisir un élément a retirer de la liste : ")
        if élément in course:
            course.remove(élément)
            print(f"{élément} a bien été retirer de la liste.")
        else:
            print(f"{élément} n'est déja pas présent dans votre liste.")
    
    elif choix_utilisateur == "3":
        if course:
            print("Voici votre liste : ")
            for i, élément in enumerate(course, 1):
                print(f"{i}. {élément}")
        else:
            print("Votre liste est vide.")
    
    elif choix_utilisateur == "4":
        course.clear()
        print("Votre liste est désormais vide.")
    
    elif choix_utilisateur == "5":
        sys.exit()

    
