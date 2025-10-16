import pandas as pd
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Chargement des variables d'environnement
load_dotenv()

def load_data_to_mysql():
    """
    Charge les données du fichier CSV dans la table MySQL
    """
    connection = None
    cursor = None
    
    try:
        # Connexion à la base de données
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Lecture des données depuis le fichier CSV
            df = pd.read_csv('data/supermarket_sales.csv')
            
            # Conversion des dates au format approprié
            df['OrderDate'] = pd.to_datetime(df['OrderDate']).dt.date
            
            # Préparation des données pour l'insertion
            data_to_insert = [tuple(row) for row in df.itertuples(index=False)]
            
            # Requête d'insertion
            insert_query = """
            INSERT INTO sales (OrderID, OrderDate, CustomerID, Product, Category, Quantity, UnitPrice, City, Region)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Insertion des données par lots
            batch_size = 1000
            for i in range(0, len(data_to_insert), batch_size):
                batch = data_to_insert[i:i+batch_size]
                cursor.executemany(insert_query, batch)
                connection.commit()
                print(f"Insertion du lot {i//batch_size + 1} ({len(batch)} enregistrements) réussie")
            
            print(f"Total de {len(df)} enregistrements insérés avec succès dans la table 'sales'")
            
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
        
    except FileNotFoundError:
        print("Erreur: Le fichier 'data/supermarket_sales.csv' n'a pas été trouvé. Exécutez d'abord le script 01_generate_data.py")
        
    finally:
        # Fermeture de la connexion
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("Connexion MySQL fermée")

if __name__ == "__main__":
    load_data_to_mysql()