import instances as INSTANCE

def jeu():
    
    print ("Bienvenue dans le jeu !")
    # Choix du nom du personnage et classe
    nom = input ("Choisissez votre nom : ").capitalize()
    choix = input ("Choisissez votre classe (avec le numero) parmis  les suivantes: 1. guerrier, 2. mage, 3. archer ")
    INSTANCE.perso.choix_classe(classe=choix , nom=nom)
    
    print("Les regles :")
    print(" ==> Vous devez combattre les monstres pour gagner de l'experience et de l'or et avancer dans la forêt.")
    print(" ==> Vous pouvez récoupérer votre vie en vous rendant au village.")
    print(" ==> Vous gagner lorsque vous avez vaincu le boss ou dans le cas contraire ... vous perdez la partie. \n")
    
    