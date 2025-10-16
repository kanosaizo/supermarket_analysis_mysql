import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Chargement des variables d'environnement
load_dotenv()

def create_database_and_tables():
    """
    Crée la base de données et la table nécessaires pour le projet
    """
    connection = None
    cursor = None
    
    try:
        # Connexion au serveur MySQL (sans spécifier de base de données)
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Création de la base de données si elle n'existe pas
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {os.getenv('DB_NAME')} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"Base de données '{os.getenv('DB_NAME')}' créée avec succès ou déjà existante")
            
            # Utilisation de la base de données
            cursor.execute(f"USE {os.getenv('DB_NAME')}")
            
            # Création de la table sales
            create_table_query = """
            CREATE TABLE IF NOT EXISTS sales (
                OrderID INT PRIMARY KEY,
                OrderDate DATE,
                CustomerID INT,
                Product VARCHAR(100),
                Category VARCHAR(50),
                Quantity INT,
                UnitPrice DECIMAL(10, 2),
                City VARCHAR(50),
                Region VARCHAR(50)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """
            
            cursor.execute(create_table_query)
            print("Table 'sales' créée avec succès ou déjà existante")
            
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
        
    finally:
        # Fermeture de la connexion
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("Connexion MySQL fermée")

if __name__ == "__main__":
    create_database_and_tables()