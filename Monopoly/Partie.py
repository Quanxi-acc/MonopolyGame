from Plateau import Plateau
from Joueur import Joueur
from Terrain import Terrain
from CaseSpeciale import CaseSpeciale
import random

class Partie:
    def __init__(self):
        # Initialise la liste des joueurs
        self.joueurs = []
        # Initialise le plateau de jeu avec les cases définies
        self.plateau = Plateau()
        # Création des joueurs via saisie utilisateur
        self.initialiser_joueurs()
        # Tour actuel (incrémenté à chaque boucle de jeu)
        self.tour_actuel = 0

    def initialiser_joueurs(self):
        """
        Demande à l'utilisateur le nombre de joueurs (entre 2 et 6),
        puis leurs noms, et crée les objets Joueur correspondants.
        """
        nb_joueurs = int(input("Combien de joueurs ? (2 à 6) : "))
        while nb_joueurs < 2 or nb_joueurs > 6:
            nb_joueurs = int(input("Nombre invalide. Choisissez entre 2 et 6 joueurs : "))

        for i in range(nb_joueurs):
            nom = input(f"Nom du joueur {i + 1} : ")
            self.joueurs.append(Joueur(nom))

    def choix_action(self, joueur):
        """
        Affiche le menu d'action du joueur et retourne le choix sélectionné.
        Gère aussi les entrées invalides.
        """
        print(f"\n{joueur.nom}, choisissez une action :")
        print("1. Lancer les dés")
        print("2. Consulter votre solde")
        print("3. Consulter vos propriétés")
        print("4. Vendre un terrain")
        print("5. Améliorer un de vos terrains")

        try:
            action = int(input("Choix : "))
            return action
        except ValueError:
            print("Entrée invalide.")
            return self.choix_action(joueur)

    def tour(self, joueur):
        """
        Gère un tour de jeu complet pour le joueur :
        déplacement, actions, paiements, etc.
        """
        if joueur.bloque:
            print(f"{joueur.nom} est bloqué ce tour à cause de la prison.")
            joueur.bloque = False
            return

        action = self.choix_action(joueur)

        if action == 1:
            # Lancer de dés et déplacement
            de1, de2 = random.randint(1, 6), random.randint(1, 6)
            total = de1 + de2
            print(f"{joueur.nom} lance les dés : {de1} + {de2} = {total}")
            joueur.deplacement(total, len(self.plateau.cases))
            self.traitement_post_deplacement(joueur)

        elif action == 2:
            print(f"{joueur.nom}, votre solde est de {joueur.argent}€.")

        elif action == 3:
            if joueur.proprietes:
                print("Vos propriétés :")
                for t in joueur.proprietes:
                    t.afficher_info()
            else:
                print("Vous ne possédez aucun terrain.")

        elif action == 4:
            joueur.vendre_terrain()

        elif action == 5:
            terrains_possedes = joueur.proprietes
            if not terrains_possedes:
                print("Vous n'avez aucun terrain à améliorer.")
                return

            print("Terrains disponibles pour amélioration :")
            for i, t in enumerate(terrains_possedes):
                print(f"{i+1}. {t.nom} - Niveau : {getattr(t, 'niveau', 0)} - Loyer actuel : {t.loyer}€")

            choix = input("Numéro du terrain à améliorer (ou rien pour annuler) : ")
            if choix.isdigit():
                choix = int(choix) - 1
                if 0 <= choix < len(terrains_possedes):
                    cout = terrains_possedes[choix].ameliorer()
                    if cout > 0 and joueur.argent >= cout:
                        joueur.argent -= cout
                    elif joueur.argent < cout:
                        print("Vous n'avez pas assez d'argent pour améliorer ce terrain.")
                else:
                    print("Numéro invalide.")
            else:
                print("Amélioration annulée.")

    def traitement_post_deplacement(self, joueur):
        """
        Détermine l'effet de la case sur laquelle le joueur a atterri.
        Gère l'achat de terrain, le paiement du loyer, ou l'effet spécial.
        """
        case = self.plateau.cases[joueur.position]
        print(f"{joueur.nom} est arrivé sur la case {case.nom}")

        if isinstance(case, Terrain):
            if case.est_achetable():
                print(f"Ce terrain est disponible pour {case.prix}€.")
                achat = input("Souhaitez-vous l'acheter ? (oui/non) : ").lower()
                if achat == "oui":
                    joueur.acheter(case)
            elif case.proprietaire and case.proprietaire != joueur:
                print(f"Ce terrain appartient à {case.proprietaire.nom}. Vous devez payer {case.loyer}€.")
                if not joueur.payer(case.loyer, case.proprietaire):
                    print(f"{joueur.nom} a été éliminé.")
                    self.joueurs.remove(joueur)

        elif isinstance(case, CaseSpeciale):
            case.activer_effet(joueur)

    def lancer(self):
        """
        Lance la boucle principale du jeu.
        Le jeu continue tant qu’il reste plus d’un joueur.
        """
        while len(self.joueurs) > 1:
            for joueur in self.joueurs[:]:  # Copie de la liste pour éviter erreurs de suppression
                self.tour(joueur)

        print(f"Le gagnant est {self.joueurs[0].nom} avec {self.joueurs[0].argent}€ !")
