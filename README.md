\# Analyse des Ventes d'un Supermarché avec Python et MySQL



Ce projet présente une analyse de bout en bout des données de ventes d'un supermarché. L'objectif est de démontrer un pipeline de données complet : de la génération de données fictives à leur stockage dans une base de données MySQL, jusqu'à l'extraction d'insights commerciaux pertinents à l'aide de Python et de techniques de visualisation.



\## Objectif du Projet



\-   Générer un jeu de données réaliste de ventes.

\-   Mettre en place une base de données MySQL et y stocker les données de manière efficace.

\-   Se connecter à la base de données depuis un environnement Python.

\-   Analyser les données pour identifier des tendances de vente, les produits les plus rentables et les variations régionales.

\-   Présenter les résultats sous forme de graphiques et d'insights textuels.



\## Technologies Utilisées



\-   Python 3

\-   MySQL (Base de données relationnelle)

\-   Bibliothèques Python:

    - pandas pour la manipulation et l'analyse de données

    - mysql-connector-python pour ce connecter à MySQL

    - faker pour générer des données fictives

    - python-dotenv (gestion des variables d'environnement)

    - matplotlib et seaborn pour la visualisation de données

    - jupyter et ipykernel (Environnement d'analyse interactif)



\## Structure du Projet



supermarket\_analysis\_mysql/

├── .env # Fichier de configuration pour la base de données

├── .gitignore # Fichiers à ignorer par Git

├── README.md # Documentation du projet

├── data/ # Dossier contenant les données générées

│ └── supermarket\_sales.csv

├── scripts/

│ ├── 01\_generate\_data.py # Génération de données fictives

│ ├── 02\_setup\_database.py # Configuration de la base de données

│ └── 03\_load\_data.py # Chargement des données dans MySQL

└── analysis/ # Notebooks d'analyse

└── sales\_analysis.ipynb



\## Auteur 



Sbai Othmane  

LinkedIn : 

GitHub :







"Ce projet est sous licence MIT" 

