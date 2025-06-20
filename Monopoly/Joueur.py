class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.argent = 1500
        self.position = 0
        self.proprietes = []
        self.bloque = False

    def deplacement(self, nb_cases, nb_cases_plateau):
        ancienne_position = self.position
        self.position = (self.position + nb_cases) % nb_cases_plateau
        if self.position < ancienne_position:
            self.argent += 200
            print(f"{self.nom} passe par Départ et reçoit 200€.")

    def acheter(self, terrain):
        if self.argent >= terrain.prix:
            self.argent -= terrain.prix
            terrain.proprietaire = self
            self.proprietes.append(terrain)
            print(f"{self.nom} a acheté {terrain.nom} pour {terrain.prix}€.")
        else:
            print(f"{self.nom} n'a pas assez d'argent pour acheter ce terrain.")

    def payer(self, montant, destinataire):
        if self.argent >= montant:
            self.argent -= montant
            destinataire.argent += montant
            print(f"{self.nom} a payé {montant}€ à {destinataire.nom}.")
            return True
        else:
            print(f"{self.nom} ne peut pas payer {montant}€ et fait faillite.")
            for terrain in self.proprietes:
                terrain.proprietaire = None
            self.proprietes.clear()
            return False

    def vendre_terrain(self):
        if not self.proprietes:
            print("Vous n'avez aucun terrain à vendre.")
            return

        print("Terrains disponibles à la vente :")
        for i, terrain in enumerate(self.proprietes):
            print(f"{i + 1}. {terrain.nom} - Valeur : {terrain.prix // 2}€")

        try:
            choix = int(input("Choisissez le numéro du terrain à vendre : ")) - 1
            if 0 <= choix < len(self.proprietes):
                terrain = self.proprietes.pop(choix)
                self.argent += terrain.prix // 2
                terrain.proprietaire = None
                print(f"{self.nom} a vendu {terrain.nom} pour {terrain.prix // 2}€.")
            else:
                print("Choix invalide.")
        except ValueError:
            print("Entrée invalide.")
