import requests
from bs4 import BeautifulSoup
import csv

# URL de base
base_url = "http://books.toscrape.com/catalogue/page-{}.html"

# Liste pour stocker les données des livres
books = []

# Boucle pour parcourir toutes les pages
for page in range(1, 51):  # 50 pages à scraper
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver les livres sur la page
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        books.append({
            'title': title,
            'price': price,
            'availability': availability
        })

# Écriture des données dans un fichier CSV
csv_file = 'books_data.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['title', 'price', 'availability'])
    writer.writeheader()
    writer.writerows(books)

print(f"Fichier CSV '{csv_file}' créé avec succès !")
