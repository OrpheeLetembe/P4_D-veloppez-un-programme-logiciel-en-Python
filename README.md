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














