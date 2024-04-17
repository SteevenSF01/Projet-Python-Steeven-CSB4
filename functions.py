import random

class Personnage:
    def __init__(self, nom="", classe="", vie=0, attaque=0, defense=0, xp=0, niveau=1, argent =0):
        self.nom = nom
        self.classe = classe
        self.hp = vie
        self.hp_max = vie
        self.attaque = attaque
        self.defense = defense
        self.exp = xp
        self.niveau = niveau
        self.argent  = argent  
        self.inventaire = Inventaire()

    def est_en_vie(self):
        return self.hp > 0

    def afficher_stats(self):
        print(f"{self.nom} - HP: {self.hp}/{self.hp_max}, Niveau: {self.niveau}, EXP: {self.exp}, Or: {self.argent }")

class Ennemi(Personnage):
    def __init__(self, nom, hp, attaque, defense, exp_recompense, or_recompense):
        super().__init__(nom, "Ennemi", hp, attaque, defense)
        self.exp_recompense = exp_recompense
        self.or_recompense = or_recompense

class Objet:
    def __init__(self, nom, effet):
        self.nom = nom
        self.effet = effet


class Inventaire:
    def __init__(self):
        self.objets = []
        self.argent  = 0

    def ajouter_objet(self, objet):
        self.objets.append(objet)

    def utiliser_objet(self, nom_objet, personnage):
        for objet in self.objets:
            if objet.nom == nom_objet:
                objet.effet(personnage)
                self.objets.remove(objet)
                return True
        return False

class Jeu:
    def __init__(self):
        self.personnage = None
        self.distance_jusqu_au_boss = random.randint(8, 12)
        self.distance_actuelle = 0

    def debutPartie(self):
        print("")
        print("██████╗ ██╗███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗██╗   ██╗███████╗")
        print("██╔══██╗██║██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║██║   ██║██╔════╝")
        print("██████╔╝██║█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║██║   ██║█████╗")
        print("██╔══██╗██║██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██╔══╝")
        print("██████╔╝██║███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝███████╗")
        print("╚═════╝ ╚═╝╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝")
        nom_personnage = input("Entrez le nom de votre héros: ")
        classe_personnage = input("Choisissez votre classe (Guerrier, Mage, Archer): ")
        self.personnage = Personnage(nom_personnage, classe_personnage, 100, 20, 10)
        self.menu_principal()

    def menu_principal(self):
        while self.personnage.est_en_vie():
            print("\nChoisissez une option parmis les suivantes: ")
            print("**************************")
            print("Menu Principal:")
            print("1. Explorer la Forêt")
            print("2. Visiter le Village")
            print("3. Vérifier les Statistiques")
            print("4. Vérifier l'Inventaire")
            print("5. Quitter le Jeu")
            print("**************************\n")
            choix = input("")

            if choix == '1':
                self.explorer_foret()
            elif choix == '2':
                self.visiter_village()
            elif choix == '3':
                self.personnage.afficher_stats()
            elif choix == '4':
                self.verifier_inventaire()
            elif choix == '5':
                print("")
                print("Aurevoir, à bientot!")
                print("")
                break 
            else:
                print("")
                print("Choix invalide.")
                print("")

    def explorer_foret(self):
        if self.distance_actuelle == self.distance_jusqu_au_boss:
            print("Preparez vous a affronter le Boss!")
            boss = Ennemi("Ericter", 200, 25, 15, 100, 200)
            self.combat(self.personnage, boss)
            if not boss.est_en_vie():
                print("Vous avez vaincu le boss!")
                print("Fin de la partie.")
                return
        else:
            self.distance_actuelle += 1
            print("**********************")
            print(f"Vous êtes à {self.distance_actuelle} km.")
            print("**********************")
            evenement = random.choice(["combat", "trouver", "rien"])
            if evenement == "combat":
                ennemi = self.generer_ennemi()
                self.combat(self.personnage, ennemi)
            elif evenement == "trouver":
                self.trouver_aleatoire()
            elif evenement == "rien":
                print("Vous etes chanceux, pas de danger à l'horizon et malheureusement pas objet trouvé")

    def visiter_village(self):
        print("Bienvenue al 'Pueblo'!")
        while True:
            print("\nChoisissez une option parmis les suivantes: ")
            print("******************************")
            print("Menu del Pueblo:")
            print("1. Dormir à l'auberge (Coûte 10 Pièces d'Or)")
            print("2. Magasin")
            print("3. Retourner au Menu Principal")
            print("******************************")
            choix = input("")
            if choix == '1':
                if self.personnage.argent  >= 10:
                    self.personnage.hp = self.personnage.hp_max
                    self.personnage.argent  -= 10
                    print("Vous avez récupéré toutes votre vie.")
                else:
                    print("Malheureusemment vous n'avez pas assez de pièces d'or.")
            elif choix == '2':
                self.magasin()
            elif choix == '3':
                break
            else:
                print("")
                print("Choix invalide.")
                print("")

    def combat(self, heros, ennemi):
        print("⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️")
        print(f"Vous aller affronter un mini boss : {ennemi.nom}")
        print("⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️")
        while heros.est_en_vie() and ennemi.est_en_vie():
            heros.afficher_stats()
            ennemi.afficher_stats()
            action = input("Choisissez une action: Attaquer (1) / Utiliser un objet (2): ")
            if action == '1':
                self.attaquer(heros, ennemi)
            elif action == '2':
                nom_objet = input("Entrez le nom de l'objet que vous voulez utiliser: ")
                if not self.personnage.inventaire.utiliser_objet(nom_objet, heros):
                    print("Objet non trouvé ou non applicable.") 
            if ennemi.est_en_vie():
                self.attaquer(ennemi, heros)

    def attaquer(self, attaquant, defenseur):
        degats = max(attaquant.attaque - defenseur.defense, 0)
        defenseur.hp -= degats
        print("💥 💥 💥 💥 💥 💥 💥 💥 💥 💥 💥")
        print(f"{attaquant.nom} attaque {defenseur.nom} et cause {degats} de dégâts!")
        print("💥 💥 💥 💥 💥 💥 💥 💥 💥 💥 💥")

    def generer_ennemi(self):
        noms_ennemis = ['ogre', 'Spectre', 'Basilics', 'Minotaure']
        nom = random.choice(noms_ennemis)
        hp = random.randint(50, 100)
        attaque = random.randint(5, 15)
        defense = random.randint(5, 10)
        exp_recompense = random.randint(5, 15)
        or_recompense = random.randint(10, 50)
        return Ennemi(nom, hp, attaque, defense, exp_recompense, or_recompense)

    def trouver_aleatoire(self):
        decouvertes = ['argent', 'objet', 'exp']
        resultat = random.choice(decouvertes)
        if resultat == 'argent':
            quantite = random.randint(10, 50)
            self.personnage.inventaire.argent  += quantite
            print("\n💸 💸 💸 💸 💸 💸 💸 💸")
            print(f"Vous avez trouvé {quantite} pièces d'argent!")
            print("💸 💸 💸 💸 💸 💸 💸 💸\n")
        elif resultat == 'objet':
            objet = Objet("potion", lambda personnage: setattr(personnage, 'hp', min(personnage.hp + 50, personnage.hp_max)))
            self.personnage.inventaire.ajouter_objet(objet)
            print("🏺🏺🏺🏺🏺🏺🏺🏺")
            print("Vous avez trouvé une potion!")
            print("🏺🏺🏺🏺🏺🏺🏺🏺")
        elif resultat == 'exp':
            quantite_exp = random.randint(5, 15)
            self.personnage.exp += quantite_exp
            print("")
            print(f"Vous avez gagné {quantite_exp} EXP!")
            print("")

    def verifier_inventaire(self):
        print("Inventaire:")
        for objet in self.personnage.inventaire.objets:
            print(objet.nom)
        print(f"Or: {self.personnage.inventaire.argent }")

    def magasin(self):
        objets_a_vendre = {
            'Potion': (5, lambda personnage: setattr(personnage, 'hp', min(personnage.hp + 50, personnage.hp_max))),
            'Super Potion': (20, lambda personnage: setattr(personnage, 'hp', personnage.hp_max))
        }
        print("Objets à la vente:")
        for objet, details in objets_a_vendre.items():
            print(f"{objet}: {details[0]} pièces d'or")
        achat = input("Choisissez l'objet que vous voulez acheter? ").capitalize()
        if achat in objets_a_vendre and self.personnage.inventaire.argent  >= objets_a_vendre[achat][0]:
            self.personnage.inventaire.argent  -= objets_a_vendre[achat][0]
            nouvel_objet = Objet(achat, objets_a_vendre[achat][1])
            self.personnage.inventaire.ajouter_objet(nouvel_objet)
            print(f"Vous avez acheter {achat}.")
        else:
            print("Pas assez de pièces d'or ou objet non trouvé.")
