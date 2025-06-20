**Programming Guidelines - Monopoly Project**

This charter describes the coding conventions we followed during the development of the Monopoly project in Python.

---

## 1. Naming

### Classes

* Class names use **CamelCase**.
* Example:

```python
class Joueur:
    ...
```

### Variables and Attributes

* Use **snake\_case** (lowercase with underscores).
* Example:

```python
nom_joueur = "Alice"
position_actuelle = 0
```

### Constants

* All uppercase letters with underscores.
* Example:

```python
PRIX_COULEURS = {"brown": 60, "blue": 100}
```

---

## 2. Code Organization

### Separate Files

Each main entity is defined in its own file:

* `Case.py` → Base class
* `Joueur.py` → Player management
* `Partie.py` → Game flow logic
* ...

### Short and Clear Methods

Each method performs **one clearly defined task**.

---

## 3. Comments

### Class and Function Headers

Each **class** and **function** is commented with a clear sentence explaining its purpose.

### Line-by-Line

In the commented version, each important line is accompanied by an **explanatory comment**.

---

## 4. Readability

* Proper indentation (4 spaces).
* Lines should not exceed 80–100 characters when possible.
* Add spaces between logical blocks (e.g., between two functions).

---

## 5. Error Handling

* Use `try/except` for user input.
* Example:

```python
try:
    nb = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number.")
```

---

## 6. Object-Oriented Programming

* The code is **structured around classes**.
* Example:

```python
class Terrain(Case):
    def __init__(self, nom, id_case, couleur):
        super().__init__(nom, id_case)
        ...
```

---

## 7. Project-Specific Conventions

* **Prices** and **rents** are based on standard color groups.
* **Special spaces** are handled separately using `CaseSpeciale`.
* We **check a player's properties** before charging them or eliminating them.
