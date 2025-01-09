Configuration de l'environnement Virtuel Création d'un environnement virtuel Pour isoler les dépendances de votre projet et éviter les conflits avec d'autres projets, il est recommandé de créer un environnement virtuel.

Ouvrez votre terminal et naviguez jusqu'au répertoire racine de votre projet.

Exécutez la commande suivante pour créer un nouvel environnement virtuel nommé venv : python -m venv venv

NB: Vous pouvez remplacer venv par le nom de votre choix.

Activation de l'environnement virtuel Sur Windows: venv\Scripts\activate

Sur Linux/macOS: source venv/bin/activate

Une fois activé, vous verrez le nom de votre environnement entre parenthèses au début de votre invite de commande.

Installation des dépendances Pour installer les packages nécessaires au fonctionnement de votre projet, exécutez la commande suivante : pip install -r requirements.txt Assurez-vous d'avoir créé un fichier requirements.txt à la racine de votre projet et d'y avoir listé toutes les dépendances.

Exécution du script Pour exécuter votre script Python, utilisez la commande python suivie du nom de votre fichier : python votre_script.py

Exemple complet:

Bash

Créer l'environnement
python -m venv venv

Activer l'environnement
venv\Scripts\activate # Pour Windows source venv/bin/activate # Pour Linux/macOS

Installer les dépendances
pip install -r requirements.txt

Exécuter le script
python scraper.py

Désactivation de l'environnement virtuel Pour désactiver l'environnement virtuel, exécutez simplement : deactivate

Structure du projet (exemple) mon_projet/ ├── venv/ # Environnement virtuel ├── requirements.txt # Liste des dépendances ├── scraper.py # Votre script Python └── images/ # Dossier pour stocker les images téléchargée
