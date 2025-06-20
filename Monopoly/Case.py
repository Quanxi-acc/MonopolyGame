class Case:
    def __init__(self, nom, id_case):
        self.nom = nom  
        self.id = id_case  

    def afficher_case(self):
        print(f"Case {self.id} : {self.nom}")
