class Personnage:
    def __init__(self, classe=None):
        self.classe = classe
        self.vie = 0
        self.maxVie = 0
        self.attaque = 0
        self.defense = 0
        self.argent = 0
        self.xp = 0
        self.niveau = 1
        self.inventaire = []
        self.equipement = []
        self.position = 'village'

    def choix_classe(self, classe, nom):
        classes = {
            "1": {"nom": "Guerrier", "vie": 300, "attaque": 20, "defense": 15},
            "2": {"nom": "Mage", "vie": 200, "attaque": 25, "defense": 10},
            "3": {"nom": "Archer", "vie": 250, "attaque": 30, "defense": 5}
        }

        if classe in classes:
            self.nom = nom
            self.vie = classes[classe]["vie"]
            self.maxVie = classes[classe]["vie"]
            self.attaque = classes[classe]["attaque"]
            self.defense = classes[classe]["defense"]
            self.classe = classes[classe]["nom"]
            self.argent = 0
            self.xp = 0
            self.niveau = 1
            self.inventaire = []
            self.equipement = []
            self.position = 'village'
            print(f"\n   Stats de votre personnage :\n   Nom :{self.nom}, classe : {self.classe}, Vie :{self.vie}, Attaque :{self.attaque}, Defense :{self.defense}\n")
        else:
            print("Classe invalide.")



class Ennemie:
    def __init__(self, nom, vie, attaque, defense, position):
        self.nom = nom
        self.vie = vie
        self.attaque = attaque
        self.defense = defense
        self.position = position