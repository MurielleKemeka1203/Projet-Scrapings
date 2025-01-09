import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# URL de la page d'accueil
base_url = "https://books.toscrape.com/"

# Créer un répertoire pour stocker les images
if not os.path.exists("images"):
    os.makedirs("images")

# Récupérer le contenu HTML de la page d'accueil
response = requests.get(base_url)
soup = BeautifulSoup(response.text, "html.parser")

# Trouver toutes les catégories (liens vers les pages de catégorie)
category_links = soup.find("ul", class_="nav").find_all("a")
categories = [a.get("href") for a in category_links]

# Fonction pour télécharger les images d'une page de catégorie
def download_images_from_category(category_url, category_name):
    # Créer un dossier pour la catégorie
    category_folder = os.path.join("images", category_name)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)

    # Récupérer le contenu HTML de la page de la catégorie
    category_page_url = urljoin(base_url, category_url)
    response = requests.get(category_page_url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouver toutes les balises <img> dans la page
    img_tags = soup.find_all("img")

    # Télécharger chaque image
    for img_tag in img_tags:
        img_url = img_tag.get("src")
        if img_url:
            # Construire l'URL complète de l'image
            img_url = urljoin(category_page_url, img_url)
            # Extraire le nom du fichier de l'URL de l'image
            img_name = os.path.join(category_folder, img_url.split("/")[-1])

            # Télécharger l'image
            try:
                img_data = requests.get(img_url).content
                with open(img_name, "wb") as img_file:
                    img_file.write(img_data)
                print(f"Image téléchargée : {img_name}")
            except requests.exceptions.RequestException as e:
                print(f"Erreur lors du téléchargement de {img_url}: {e}")

# Boucle sur chaque catégorie
for category_url in categories:
    # Extraire le nom de la catégorie depuis l'URL
    category_name = category_url.split("/")[-2]
    download_images_from_category(category_url, category_name)

print("Téléchargement des images terminé.")
