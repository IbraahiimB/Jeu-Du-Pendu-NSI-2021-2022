import random

liste_mots = ["famille","premier","accident","travail","village"]
random.choice(liste_mots)

solution = random.choice(liste_mots)
tentatives_restantes = 7
affichage = ""
lettres_validées = ""

for l in solution:
    affichage += "_ "
    
while tentatives_restantes > 0:
    print("MOT A TROUVER:", affichage)
    proposition = input("Entrez une lettre: ")

    if proposition in solution:
        lettres_validées += proposition
        print("La/Les lettre(s)",proposition,"est/sont dans le mot")
    else:
        tentatives_restantes -= 1
        print("La/Les lettre(s)", proposition, "n'est/ne sont pas dans le mot")
        print("tentatives restantes: ", tentatives_restantes)
        if tentatives_restantes <= 0:
            print(" |======Y= ")
        if tentatives_restantes <= 1:
            print(" ||     |  ")
        if tentatives_restantes <= 2:
            print(" ||     °        YOU ARE DEAD!")
        if tentatives_restantes <= 3:
            print(" ||    /|\  ")
        if tentatives_restantes <= 4:
            print(" ||    /|\  ")
        if tentatives_restantes <= 5:
            print("/||         ")
        if tentatives_restantes <= 6:
            print("============")
    affichage = ""
    for x in solution:
        if x in lettres_validées:
            affichage += x + " "
        else:
            affichage += "_ "
            
    if "_" not in affichage:
        print("! Victoire !")
        break
    

   
    

