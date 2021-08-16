# Programme de gestion de tournoi d’échec suivant le système suisse

# Description :
Le programme de gestion de tournoi d’échec est développé en python 3.9.5. il a pour but de palier aux difficultés rencontrées par les membres du club avec leur système de gestion actuel, notamment les panes récurrentes et les problèmes de connexion à Internet.

Le programme de gestion de tournoi d’échec permet la gestion complète d’un tournoi : 
* Création d’un nouveau tournoi, 
* Enregistrement des joueurs via une section dédiée à l'ajout de joueurs ou depuis la liste des joueurs déjà enregistrés, 
* L’appariement des joueurs selon le système suisse (chaque joueur sera opposé à un adversaire qui a fait, jusqu'à présent, aussi bien (ou mal) que lui), 
* L’attribution des points après chaque match
* L’ajout de commentaires
* Enregistrement des tournois. Les tournois peuvent se déroulés sur plusieurs jours, les dates des tournois et des rounds sont gérées automatiquement
* Mise à jour du classement des joueurs à tout moment pendant le déroulement d’un tournoi
* Visualisation des différents rapports
  *  Liste de tous les joueurs, par ordre alphabétique ou par classement.
  *  Liste de tous les joueurs d'un tournoi par ordre alphabétique ou par classement
  *  Liste de tous les tournois.
  * Liste de tous les rounds d'un tournoi.
  * Liste de tous les matchs d'un tournoi.


# Environnement virtuel :

## Création :
Pour la procédure décrite ci-dessous vous devez disposer au minimum de la version Python 3.3. Ouvrir un terminal et créer l’environnement virtuel à la racine du programme.
* Sur Windows : python -m venv <non de l’environnement>
* Sur Unix et MacOS : python3 -m venv <non de l’environnement>
## Activation :
* Sur Windows, : env\Scripts\activate
* Sur Unix et MacOS : source tutorial-env/bin/activate (Ce script est écrit pour le shell bash. Si vous utilisez csh ou fish, utilisez les variantes activate.csh ou activate.fish.)

## Installation des paquets nécessaires :

pip install -r requirements.txt

# Exécution du programme
Lancement :
* Sur Windows: python chess_program.py
* Sur Unix et MacOS : python3 python chess_program.py

# Navigation :
Une fois le programme lancé, l'utilisateur dispose de plusieurs menus : 
## Menu principal
1. création de nouveau tournoi : 
Permet la création d’un nouveau tournoi, entrée les données relatives au tournoi et aux différents joueurs. L’utilisateur est ensuite redirigé vers le menu secondaire.
2. afficher la liste des tournois :
L’utilisateur est redirigé vers le menu des tournois enregistrés
3. afficher la liste des joueurs :
L’utilisateur est redirigé vers la liste des joueurs enregistrés, il peut ainsi afficher les joueurs par ordre alphabétique ou par classement.
4. quitter le programme

## Menu secondaire
1. ajouter les résultats des matchs :
L’utilisateur est redirigé vers la session de désignation du vainqueur de chaque match d’un round. Les points sont ensuite attribués selon le système établi (1 pour le vainqueur, 0.5 à chaque joueur en cas de match nul et 0 pour le perdant.
2. mises à jour du classement :
L’utilisateur est invité à sélectionner un joueur de liste des joueurs du tournoi, il peut ensuite mettre à jour le classement de celui-ci. 
3. ajouter un commentaire
4. sauvegarder :
Enregistrement / mise à jour du tournoi dans la base de données
5. aller au menu principal

## Menu des tournois enregistrés
1. afficher la liste des joueurs
L’utilisateur est redirigé vers la liste des joueurs du tournoi, il peut ainsi afficher les joueurs par ordre alphabétique ou par classement.
2. afficher la liste des rounds et des matchs
3. quitter
4. continuer le tournoi (si celui-ci n’est pas terminer)

## Génération du rapport flake8_html
Ouvrir un terminal et lancer la commande
flake8 controllers models views chess_program.py --format=html --htmldir=flake-report

















