# TP  Extraction de données avec Selenium et Page Object Model

## Contexte

Vous devez automatiser l’exploration du site suivant :

`https://books.toscrape.com`

L’objectif est de récupérer des informations sur les livres affichés sur la page d’accueil, puis de produire un petit rapport en console.

Ce TP doit être réalisé en **Python** avec **Selenium**, en appliquant le principe du **Page Object Model (POM)**.

---

## Objectif pédagogique

Ce TP a pour but de vous faire pratiquer :

* l’utilisation de Selenium avec Python ;
* l’attente du chargement d’une page ;
* l’extraction de données depuis plusieurs éléments d’une page ;
* la structuration d’un script avec le **Page Object Model**.

---

## Travail demandé

### 1. Préparer le projet

Créer un projet Python permettant de lancer un navigateur Chrome avec Selenium.

---

### 2. Mettre en place une structure POM

Créer au moins une classe représentant la page principale du site.

Cette classe devra permettre de :

* charger la page ;
* attendre que les livres soient disponibles ;
* récupérer les éléments nécessaires à l’extraction.

---

### 3. Extraire les données

Depuis la page d’accueil, récupérer pour chaque livre affiché les informations utiles.

Vous stockerez les données extraites dans une structure adaptée.

---

### 4. Générer un rapport

Afficher dans la console un compte rendu contenant au minimum :

* le nombre total de livres récupérés ;
* les informations des premiers livres extraits ;
* quelques statistiques simples sur les données collectées.

---


## Résultat attendu

À la fin du TP, l’exécution du programme doit :

* ouvrir le site `books.toscrape.com`
* récupérer les données des livres présents sur la page
* afficher un rapport clair dans la console

