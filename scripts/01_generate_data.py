import pandas as pd
import random
from faker import Faker
import os

# Initialisation de Faker en français
fake = Faker('fr_FR')

# Création du dossier data s'il n'existe pas
os.makedirs('data', exist_ok=True)

# Définition des catégories de produits et des produits associés
categories = {
    'Alimentaire': ['Pain', 'Lait', 'Fromage', 'Yaourt', 'Pâtes', 'Riz', 'Œufs', 'Beurre', 'Sucre', 'Farine'],
    'Boissons': ['Eau minérale', 'Jus de fruits', 'Soda', 'Café', 'Thé', 'Bière', 'Vin rouge', 'Vin blanc', 'Champagne', 'Limonade'],
    'Fruits et Légumes': ['Pommes', 'Bananes', 'Oranges', 'Tomates', 'Salade', 'Carottes', 'Poivrons', 'Courgettes', 'Fraises', 'Raisins'],
    'Produits ménagers': ['Lessive', 'Produit vaisselle', 'Sacs poubelle', 'Éponges', 'Javel', 'Nettoyant vitres', 'Aérosol', 'Balai', 'Serpillière', 'Gants'],
    'Hygiène et Beauté': ['Shampoing', 'Gel douche', 'Dentifrice', 'Brosse à dents', 'Déodorant', 'Rasoir', 'Crème hydratante', 'Savon', 'Parfum', 'Maquillage'],
    'Boulangerie-Pâtisserie': ['Baguette', 'Croissant', 'Pain au chocolat', 'Éclair', 'Tarte', 'Gâteau', 'Cookies', 'Muffins', 'Pain de mie', 'Viennoiseries'],
    'Viandes et Poissons': ['Poulet', 'Bœuf', 'Porc', 'Agneau', 'Saumon', 'Thon', 'Crevettes', 'Dinde', 'Jambon', 'Saucisses'],
    'Surgelés': ['Pizza', 'Glaces', 'Frites', 'Légumes surgelés', 'Fruits surgelés', 'Plats préparés', 'Poissons panés', 'Nuggets', 'Desserts', 'Pains']
}

# Liste des régions et villes françaises
regions_villes = {
    'Île-de-France': ['Paris', 'Boulogne-Billancourt', 'Saint-Denis', 'Versailles', 'Créteil'],
    'Auvergne-Rhône-Alpes': ['Lyon', 'Grenoble', 'Saint-Étienne', 'Clermont-Ferrand', 'Annecy'],
    'Hauts-de-France': ['Lille', 'Amiens', 'Roubaix', 'Tourcoing', 'Dunkerque'],
    'Nouvelle-Aquitaine': ['Bordeaux', 'Limoges', 'Poitiers', 'Pau', 'La Rochelle'],
    'Occitanie': ['Toulouse', 'Montpellier', 'Nîmes', 'Perpignan', 'Béziers'],
    'Pays de la Loire': ['Nantes', 'Angers', 'Le Mans', 'Saint-Nazaire', 'La Roche-sur-Yon'],
    'Provence-Alpes-Côte d\'Azur': ['Marseille', 'Nice', 'Toulon', 'Avignon', 'Cannes'],
    'Grand Est': ['Strasbourg', 'Reims', 'Metz', 'Mulhouse', 'Nancy'],
    'Bretagne': ['Rennes', 'Brest', 'Quimper', 'Saint-Malo', 'Vannes'],
    'Normandie': ['Rouen', 'Le Havre', 'Caen', 'Cherbourg', 'Évreux']
}

# Génération des données
data = []
order_id = 1

for _ in range(5000):
    # Sélection aléatoire d'une région et d'une ville
    region = random.choice(list(regions_villes.keys()))
    city = random.choice(regions_villes[region])
    
    # Sélection aléatoire d'une catégorie et d'un produit
    category = random.choice(list(categories.keys()))
    product = random.choice(categories[category])
    
    # Génération des autres données
    order_date = fake.date_between(start_date='-2y', end_date='today')
    customer_id = fake.random_int(min=1000, max=9999)
    quantity = random.randint(1, 20)
    unit_price = round(random.uniform(0.5, 50.0), 2)
    
    data.append({
        'OrderID': order_id,
        'OrderDate': order_date,
        'CustomerID': customer_id,
        'Product': product,
        'Category': category,
        'Quantity': quantity,
        'UnitPrice': unit_price,
        'City': city,
        'Region': region
    })
    
    order_id += 1

# Création du DataFrame
df = pd.DataFrame(data)

# Sauvegarde des données dans un fichier CSV
df.to_csv('data/supermarket_sales.csv', index=False)

print(f"Généré {len(df)} enregistrements de ventes dans data/supermarket_sales.csv")