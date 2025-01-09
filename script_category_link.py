import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

url = "http://books.toscrape.com/"

# Envoie d'une requête HTTP pour récupérer la page
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Les liens (balises <a>)
links = soup.find_all('a')

# Filtrer les liens vers les catégories et les livres
category_links = []
book_links = []
for link in links:
    # Vérifier si le lien pointe vers une page HTML (exclure les fichiers CSS, JS, etc.)
    if link.get('href') and link.get('href').endswith('.html'):
        # Vérifier si le lien est vers une catégorie ou un livre (vous pouvez ajuster cette logique en fonction de la structure du site)
        if "category" in link.get('href'):
            category_links.append(link.get('href'))
        else:
            book_links.append(link.get('href'))

# Afficher les liens extraits
print("Liens vers les catégories :", category_links)
print("Liens vers les livres :", book_links)