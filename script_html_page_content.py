import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

def scraper_page_accueil(url):
    """
    Cette fonction récupère le contenu HTML de la page d'accueil d'un site web.

    Args:
        url (str): L'URL de la page d'accueil.

    Returns:
        BeautifulSoup: Un objet BeautifulSoup représentant le contenu HTML.
    """
    response = requests.get(url)

    if response.ok:
        print(response.text)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vérifie si la requête s'est bien passée

        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de la requête : {e}")
        return None

# Accès à la page d'accueil
url = "https://books.toscrape.com/"  # l'URL de la page d'accueil
soup = scraper_page_accueil(url)

if soup:
    # On peut maintenant utiliser BeautifulSoup pour parcourir le contenu HTML
    # Par exemple, si on veut trouver tous les titres h1 :
    titres = soup.find_all('h1')
    for titre in titres:
        print(titre.text)


   