from Case import Case

class CaseSpeciale(Case):
    def __init__(self, nom, id_case, effet="aucun"):
        
        super().__init__(nom, id_case)
        self.effet = effet  

    def activer_effet(self, joueur):
        """
        Applique un effet spécifique au joueur en fonction du nom de la case spéciale.
        Chaque nom déclenche une logique différente.
        """
        if self.nom == "Départ":
            joueur.argent += 200
            print(f"{joueur.nom} passe par Départ et gagne 200€ !")
        elif self.nom == "Prison":
            joueur.bloque = True
            print(f"{joueur.nom} est en prison ! Il passe son prochain tour.")
        elif self.nom == "Police":
            joueur.argent -= 100
            print(f"{joueur.nom} est contrôlé par la police et perd 100€.")
        elif self.nom == "Parking":
            print(f"{joueur.nom} est sur la case Parking. Repos gratuit.")
        else:
            print(f"{joueur.nom} est sur une case spéciale sans effet défini.")
