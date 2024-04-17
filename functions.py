import instances as INSTANCE

def jeu():
    
    print ("Bienvenue dans le jeu !")
    # Choix du nom du personnage et classe
    nom = input ("Choisissez votre nom : ")
    choix = input ("Choisissez votre classe parmis les suivantes: 1. guerrier, 2. mage, 3. archer ")
    INSTANCE.perso.choix_classe(classe=choix , nom=nom)
    