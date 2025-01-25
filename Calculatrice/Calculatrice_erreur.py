#Déclaration de nos variables
a = b = " "

#On lance une boucle tant que a et b ne sont pas des nombres
while not (a.isdigit() and b.isdigit()):
    a = input ("Entrer un nombre : ")
    b = input ("Entrer un nombre : ")

    if not (a.isdigit() and b.isdigit()):
        print("Veuillez entrer deux nombres valides.")

#On effectue le calcul et on affiche le résultat
print(f"Le résultat de {a} + {b} est égale à {int(a) + int(b)}.")
