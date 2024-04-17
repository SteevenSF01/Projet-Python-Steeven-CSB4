class Personnage:
    def __init__(self, nom, classe=None):
        self.nom = nom
        self.classe = classe
        self.vie = 0
        self.attaque = 0
        self.defense = 0
        self.argent = 0
        self.xp = 0
        self.niveau = 1
        self.inventaire = []
        self.equipement = []
        self.position = 'village'

    def choix_classe(self, classe , nom):
        if classe == "1":
            self.nom = nom
            self.vie = 300
            self.attaque = 20
            self.defense = 15
            self.argent = 0
            self.xp = 0
            self.niveau = 1
            self.inventaire = []
            self.equipement = []
            self.position = 'village'
            print(f"    \n   Stats de votre personnage :\n   Nom :{self.nom}, Vie :{self.vie}, Attaque :{self.attaque}, Defense :{self.defense} \n")
        elif classe == "2":
            self.nom = nom
            self.vie = 200
            self.attaque = 25
            self.defense = 10
            self.argent = 0
            self.xp = 0
            self.niveau = 1
            self.inventaire = []
            self.equipement = []
            self.position = 'village'
            print(f"    \n   Stats de votre personnage :\n   Nom :{self.nom}, Vie :{self.vie}, Attaque :{self.attaque}, Defense :{self.defense} \n")
        elif classe == "3":
            self.nom = nom
            self.vie = 250
            self.attaque = 30
            self.defense = 5
            self.argent = 0
            self.xp = 0
            self.niveau = 1
            self.inventaire = []
            self.equipement = []
            self.position = 'village'
            print(f"    \n   Stats de votre personnage :\n   Nom :{self.nom}, Vie :{self.vie}, Attaque :{self.attaque}, Defense :{self.defense} \n")


class Ennemie:
    def __init__(self, nom, vie, attaque, defense, position):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque
        self.defense = defense
        self.position = position