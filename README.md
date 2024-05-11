# Interface Graphique pour Analyse de Données CSV avec Architecture MVC

![Interface Graphique](https://i.ibb.co/9cDRhBY/Screenshot-2024-05-09-173939.png)

## Description

Ce projet vise à développer une interface graphique pour un Logiciel de Manipulation de Langage (LLM) qui analyse les fichiers CSV afin de répondre aux questions des utilisateurs sur la base de données. L'interface permet également d'afficher des graphiques et du code Python utilisant la bibliothèque Pandas pour l'analyse de données.

## Architecture

Le projet suit une architecture Modèle-Vue-Contrôleur (MVC) pour une meilleure organisation et maintenabilité du code.

- **Modèle (`model.py`)** : Gère la logique métier et l'accès aux données. Charge les fichiers CSV, les stocke en mémoire et fournit des méthodes pour accéder aux données chargées.

- **Vue (`view.py`)** : S'occupe de l'interface utilisateur. Utilise la bibliothèque Streamlit pour créer une interface graphique conviviale. Affiche les données chargées et les résultats des analyses.

- **Contrôleur (`controller.py`)** : Fait le lien entre le modèle et la vue. Traite les entrées utilisateur, invoque les opérations appropriées du modèle et contrôle l'affichage des données dans la vue.

## Fonctionnalités

- **Affichage de Données** : L'interface permet de charger et d'afficher des fichiers CSV.
- **Analyse de Données** : Les utilisateurs peuvent poser des questions sur les données CSV et obtenir des réponses en utilisant un modèle de langage (LLM). Les réponses sont générées en utilisant la bibliothèque Pandas.
- **Affichage de Graphiques** : Les résultats de l'analyse peuvent être affichés sous forme de graphiques pour une meilleure visualisation des données.
- **Affichage du Code Python** : Le code Python utilisé pour l'analyse des données est également affiché pour une transparence totale.

## Développement

Pour exécuter localement le projet, assurez-vous d'avoir installé les dépendances.

Pour exécuter l'application, exécutez `main.py`.
