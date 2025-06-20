from CaseSpeciale import CaseSpeciale
from Terrain import Terrain

class Plateau:
    def __init__(self):
        self.cases = [
            CaseSpeciale("Départ", 0),
            Terrain("Boulevard de Belleville", 1, "marron"),
            Terrain("Rue Lecourbe", 2, "marron"),
            CaseSpeciale("Gare", 3),
            Terrain("Rue de Vaugirard", 4, "bleu"),
            Terrain("Rue de Courcelles", 5, "bleu"),
            Terrain("Avenue de la République", 6, "bleu"),
            CaseSpeciale("Prison", 7),
            Terrain("Boulevard de la Villette", 8, "rose"),
            Terrain("Avenue de Neuilly", 9, "rose"),
            Terrain("Rue de Paradis", 10, "rose"),
            Terrain("Avenue de Mozart", 11, "orange"),
            Terrain("Boulevard Saint-Michel", 12, "orange"),
            Terrain("Place Pigalle", 13, "orange"),
            CaseSpeciale("Parking", 14),
            Terrain("Avenue Matignon", 15, "rouge"),
            Terrain("Boulevard Malesherbes", 16, "rouge"),
            Terrain("Avenue Henri-Martin", 17, "rouge"),
            Terrain("Faubourg Saint-Honoré", 18, "jaune"),
            Terrain("Place de la Bourse", 19, "jaune"),
            Terrain("Rue La Fayette", 20, "jaune"),
            CaseSpeciale("Police", 21),
            Terrain("Avenue de Breteuil", 22, "vert"),
            Terrain("Avenue Foch", 23, "vert"),
            Terrain("Boulevard Capucines", 24, "vert"),
            CaseSpeciale("Gare Saint-Lazare", 25),
            Terrain("Avenue des Champs", 26, "violet"),
            Terrain("Rue de la Paix", 27, "violet")
        ]

    def afficher_plateau(self):
        for case in self.cases:
            case.afficher_case()
