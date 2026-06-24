import sqlite3
from tabulate import tabulate

def inspecter_base_sqlite(nom_fichier):
    conn = None
    try:
        # Connexion à la base de données SQLite
        conn = sqlite3.connect(nom_fichier)
        cursor = conn.cursor()

        # 1. Récupérer toutes les tables de la base (en excluant les tables système de SQLite)
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
        )
        tables = cursor.fetchall()

        if not tables:
            print(
                f"La base de données '{nom_fichier}' ne contient aucune table."
            )
            return

        print(f"==================================================")
        print(f" ANALYSE DE LA BASE : {nom_fichier}")
        print(f"==================================================")
        print(f"Nombre de tables détectées : {len(tables)}\n")

        # 2. Parcourir et afficher le contenu de chaque table
        for table_name in tables:
            nom_table = table_name[0]

            print(f"Table : {nom_table}")

            # Récupérer les informations sur les colonnes
            cursor.execute(f"PRAGMA table_info({nom_table});")
            colonnes = [info[1] for info in cursor.fetchall()]

            # Récupérer toutes les lignes (données) de la table
            cursor.execute(f"SELECT * FROM {nom_table};")
            lignes = cursor.fetchall()

            if not lignes:
                print("   [Table vide]\n")
            else:
                # Affichage propre du tableau grâce à tabulate
                # Le format 'grid' dessine des bordures claires autour des cellules
                print(tabulate(lignes, headers=colonnes, tablefmt="grid"))
                print("\n")

    except sqlite3.Error as e:
        print(f"Erreur lors de la lecture de la base SQLite : {e}")

    finally:
        # Fermeture sécurisée de la connexion
        if conn:
            conn.close()


# --- Zone de configuration et d'exécution ---
if __name__ == "__main__":
    # Remplace ici par le chemin ou le nom de ton fichier .db ou .sqlite
    chemin_bdd = ".local/share/newsboat/cache.db"

    inspecter_base_sqlite(chemin_bdd)
