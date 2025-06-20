**Technical Documentation - Monopoly Project (Python)**

---

### Project Goal

Create a simplified Monopoly game in Python to learn object-oriented programming (OOP).

---

### General Structure

The project is organized into multiple Python files, each with a specific role:

* `Case.py`: Base class for all board spaces
* `Terrain.py`: Class for purchasable properties
* `CaseSpeciale.py`: Manages special spaces like Jail, Parking, Police...
* `Joueur.py`: Manages player state and actions
* `Plateau.py`: Structure containing all board spaces
* `Partie.py`: Main game logic
* `main.py`: Game startup
* `Test.py`: Used for testing

---

### 1. Case.py

**Main content:**

```python
class Case:
    def __init__(self, nom, id_case):
        self.nom = nom
        self.id = id_case
```

**Details:**

* `Case` is the parent class for other types of spaces.
* `nom`: Displayed name (e.g., "Start", "Jail").
* `id_case`: Position of the space on the board.

---

### 2. Terrain.py

**Class definition:**

```python
class Terrain(Case):
    def __init__(self, nom, id_case, couleur, prix, loyer):
        super().__init__(nom, id_case)
        self.couleur = couleur
        self.prix = prix
        self.loyer = loyer
        self.proprietaire = None
```

**Details:**

* Inherits from `Case`.
* `couleur`: Used to group properties.
* `prix`: Purchase cost.
* `loyer`: Rent to pay if another player lands on it.
* `proprietaire`: `None` if not owned.

---

### 3. CaseSpeciale.py

**Example of a special space:**

```python
class CaseSpeciale(Case):
    def __init__(self, nom, id_case, effet):
        super().__init__(nom, id_case)
        self.effet = effet

    def activer_effet(self, joueur):
        if self.effet == "depart":
            joueur.argent += 200
        elif self.effet == "police":
            joueur.argent -= 100
        elif self.effet == "prison":
            joueur.bloque = True
```

**Details:**

* Manages non-purchasable spaces.
* `effet` can be `"depart"`, `"police"`, `"prison"`, etc.
* `activer_effet(joueur)` applies an effect based on the space type.

---

### 4. Joueur.py

**Simplified player class:**

```python
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.argent = 1500
        self.position = 0
        self.proprietes = []
        self.bloque = False
```

**Available actions:**

* **Move:**

```python
def deplacement(self, nb_cases, nb_cases_plateau):
    ancienne = self.position
    self.position = (self.position + nb_cases) % nb_cases_plateau
    if self.position < ancienne:
        self.argent += 200  # Passed "Start"
```

* **Buy a property:**

```python
def acheter(self, terrain):
    if self.argent >= terrain.prix:
        self.argent -= terrain.prix
        terrain.proprietaire = self
        self.proprietes.append(terrain)
```

* **Pay another player:**

```python
def payer(self, montant, destinataire):
    if self.argent >= montant:
        self.argent -= montant
        destinataire.argent += montant
```

---

### 5. Plateau.py

**Example:**

```python
class Plateau:
    def __init__(self):
        self.cases = [
            CaseSpeciale("Start", 0, "depart"),
            Terrain("Rue de la Paix", 1, "blue", 300, 50),
            CaseSpeciale("Police", 2, "police"),
            Terrain("Rue Lecourbe", 3, "orange", 180, 20),
            CaseSpeciale("Jail", 4, "prison"),
        ]
```

**Details:**

* The `self.cases` list contains all the board spaces.
* Their order defines their position on the board.

---

### 6. Partie.py

**Content:**

```python
class Partie:
    def __init__(self, joueurs, plateau):
        self.joueurs = joueurs
        self.plateau = plateau
        self.tour = 0
```

**Main method:**

```python
def tour_de_jeu(self, joueur):
    if joueur.bloque:
        print(f"{joueur.nom} is in jail this turn.")
        joueur.bloque = False
        return

    de = randint(1, 6)
    joueur.deplacement(de, len(self.plateau.cases))
    case = self.plateau.cases[joueur.position]

    if isinstance(case, Terrain):
        if case.proprietaire is None:
            choix = input("Do you want to buy this property? (y/n)")
            if choix == "y":
                joueur.acheter(case)
        elif case.proprietaire != joueur:
            loyer = case.loyer
            joueur.payer(loyer, case.proprietaire)
    elif isinstance(case, CaseSpeciale):
        case.activer_effet(joueur)
```

---

### 7. main.py

**Main function:**

```python
def main():
    plateau = Plateau()
    joueurs = [Joueur("Alice"), Joueur("Bob")]
    partie = Partie(joueurs, plateau)

    while len(partie.joueurs) > 1:
        joueur_actuel = partie.joueurs[partie.tour % len(partie.joueurs)]
        partie.tour_de_jeu(joueur_actuel)
        partie.tour += 1
```

* Starts a game with 2 players.
* Runs the game loop and calls the turn logic for each player.

---

### Global Operation

1. The game starts via `main.py`
2. Players and board are initialized
3. Each player takes a turn: movement, action depending on the space
4. If a player runs out of money, they're eliminated
5. The last remaining player wins the game
