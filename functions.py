import instances as INSTANCE

def jeu():
    
    while INSTANCE.personnage.vie <1 or INSTANCE.boss.vie < 1:
    
        print("")
        print("██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗   ██╗███████╗")
        print("██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║   ██║██╔════╝")
        print("██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║   ██║█████╗")
        print("██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██╔══╝")
        print("██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝███████╗")
        print("╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝")
        
        nom = input ("Choisissez votre nom : ").capitalize()
        
        while True:
            choix = int(input ("Choisissez votre classe (avec le numero) parmis  les suivantes: 1. guerrier, 2. mage, 3. archer "))
            if choix >= 1 and choix <= 3:
                break
            else:
                print("Veuillez choisir une classe valide")

        INSTANCE.personnage.choix_classe(classe=str(choix) , nom=nom)
        
        print("Les regles :")
        print(" ==> Vous devez combattre les monstres pour gagner de l'experience et de l'or et avancer dans la forêt.")
        print(" ==> Vous pouvez récoupérer votre vie en vous rendant au village.")
        print(" ==> Vous gagner lorsque vous avez vaincu le boss ou dans le cas contraire ... vous perdez la partie. \n")
        
        print("Que souhaitez vous faire, choisissez parmis les options suivantes :")
        choixMainMenu = int(input(" 1. Explore la forêt\n 2. Aller au village\n 3. Afficher les stats\n 4. Afficher l'inventaire\n 5. Quitter la partie \n"))
        while True:
            if choixMainMenu >= 1 and choixMainMenu <= 5:
                INSTANCE.personnage.choixMainMenu(choix=str(choixMainMenu))
                break
            else:
                print("Veuillez choisir une option valide")
        if choixMainMenu == 5:
            print("Aurevoir, à bientot")
            break