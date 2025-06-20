# Monopoly Project - BTS SIO 1st Year

## Overview

This project was developed as part of the **1st year BTS SIO** training program (IT Services for Organizations).
It is a **simplified, text-based version of the Monopoly game**, entirely coded in **Python** using an object-oriented architecture (OOP).

## Objectives

* Apply the fundamental principles of OOP
* Learn how to develop a project with multiple shared files and classes
* Manage interactions between player / board / game turn
* Implement a user-friendly logic so that the game is easy to understand, pick up, and play

## Features

* Choose the **number of players** (2 to 6)
* Turn-based gameplay including:

  * Dice rolling
  * Moving around the board
  * Buying properties
  * Paying rent
  * Selling properties
  * Automatic mortgage in case of insufficient funds
  * Management of jail and special squares (Police, Free Parking, etc.)
* Automatic end of the game when only one player remains

## Project Structure

The project is divided into several modules:

* `Case.py`: base class for all board spaces
* `CaseSpeciale.py`: inherits from `Case`, represents spaces like Start, Jail, Police, etc.
* `Terrain.py`: inherits from `Case`, represents purchasable properties
* `Joueur.py`: class representing a player (money, properties, actions...)
* `Plateau.py`: initializes and structures the game board
* `Partie.py`: manages the entire game session
* `main.py`: entry point of the program
