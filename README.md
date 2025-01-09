# Projet de Scraping - Extraction des Images du Site Books to Scrape

Ce projet permet d'extraire les images de livres présentes sur le site [Books to Scrape](http://books.toscrape.com/). Il récupère les images de chaque catégorie de livres du site et les enregistre dans un fichier CSV avec les liens vers les images.

## Fonctionnalités
- Scraper toutes les images disponibles sur le site.
- Enregistrer les informations (liens d'images) dans un fichier CSV.
- Organiser les images par catégorie de livre.

## Prérequis
Avant d'exécuter ce projet, assurez-vous que vous avez installé les outils suivants :

- **Python 3.13.1** : Assurez-vous d'avoir une version récente de Python installée sur votre machine.
- **Bibliothèques Python** :
  - `requests` : Pour effectuer des requêtes HTTP et télécharger les pages web.
  - `BeautifulSoup4` : Pour analyser le contenu HTML des pages.
  - `pandas` : Pour gérer les données et sauvegarder les résultats dans un fichier CSV.

Vous pouvez installer les dépendances requises via `pip` :
pip install requests beautifulsoup4 pandas

Installation
Clonez ce repository sur votre machine locale en exécutant la commande suivante :
git clone https://github.com/USERNAME/gestion-de-projet-csv.git
Accédez au répertoire du projet :
cd Projet-Scrapings-csv
Utilisation
Lancer le script de scraping :
Exécutez le script Python pour démarrer l'extraction des images.
python scrape_images.py
Résultat :
Les images des livres seront extraites et enregistrées dans un fichier CSV .

Le projet contient les fichiers suivants :
- scrape_books.py      # Script principal pour extraire les données
- images_books.csv     # Fichier CSV contenant les liens vers les images extraites
- README.md            # Ce fichier de documentation
Comment ça marche ?
Le script scrape_books.py effectue une requête HTTP pour accéder à la page d'accueil du site Books to Scrape.
Ensuite, il parcourt les différentes catégories de livres présentes sur le site.
Pour chaque catégorie, il extrait les informations des livres, y compris les liens vers les images.
Les données extraites sont stockées dans un fichier CSV, où chaque ligne contient les informations sur un livre et son image.
Les images sont récupérées à partir de leurs URLs et peuvent être téléchargées si nécessaire.
