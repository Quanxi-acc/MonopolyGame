from Case import Case

PRIX_COULEURS = {
    "marron": {"coutAchat": 60, "loyer": 40},
    "bleu": {"coutAchat": 100, "loyer": 80},
    "rose": {"coutAchat": 140, "loyer": 120},
    "orange": {"coutAchat": 180, "loyer": 160},
    "rouge": {"coutAchat": 220, "loyer": 200},
    "jaune": {"coutAchat": 260, "loyer": 240},
    "vert": {"coutAchat": 300, "loyer": 280},
    "violet": {"coutAchat": 350, "loyer": 330}
}

class Terrain(Case):
    def __init__(self, nom, id_case, couleur):
        super().__init__(nom, id_case)
        self.couleur = couleur
        self.prix = PRIX_COULEURS[couleur]["coutAchat"]
        self.loyer = PRIX_COULEURS[couleur]["loyer"]
        self.proprietaire = None
        self.niveau = 0  
    def est_achetable(self):
        return self.proprietaire is None

    def afficher_info(self):
        proprio = self.proprietaire.nom if self.proprietaire else "Personne"
        print(f"{self.nom} - Couleur : {self.couleur} - Prix : {self.prix}€ - Loyer : {self.loyer}€ - Niveau : {self.niveau} - Propriétaire : {proprio}")

    def ameliorer(self):
        """
        Améliore le terrain en augmentant le loyer selon le niveau.
        Retourne le coût de l'amélioration ou 0 si le niveau max est atteint.
        """
        if self.niveau >= 5:
            print("Niveau maximal atteint pour ce terrain.")
            return 0

        cout = 50 * (self.niveau + 1)
        self.niveau += 1
        self.loyer = int(self.loyer * 1.5)  
        print(f"{self.nom} est amélioré au niveau {self.niveau}. Nouveau loyer : {self.loyer}€.")
        return cout
