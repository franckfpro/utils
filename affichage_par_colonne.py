import argparse
from pathlib import Path
import itertools

def afficher_colonnes_dossiers(chemin_dossier):
    dossier_base = Path(chemin_dossier)
    
    # Vérification que l'argument est bien un dossier existant
    if not dossier_base.is_dir():
        print(f"Erreur: le chemin '{chemin_dossier}' n'est pas un dossier valide.")
        return

    colonnes = {}
    
    # Récupération des sous-dossiers et de leurs fichiers
    for element in dossier_base.iterdir():
        if element.is_dir():
            # On liste uniquement les fichiers contenus dans ce sous-dossier
            fichiers = [f.name for f in element.iterdir() if f.is_file()]
            colonnes[element.name] = fichiers
            
    if not colonnes:
        print("Erreur: aucun sous-dossier trouvé dans ce répertoire.")
        return

    # Calcul de la largeur de chaque colonne pour un affichage aligné
    largeurs_colonnes = {}
    for dossier, fichiers in colonnes.items():
        largeur_max = len(dossier)
        if fichiers:
            largeur_max = max(largeur_max, max(len(f) for f in fichiers))
        # Ajout d'une marge de 3 caractères entre les colonnes
        largeurs_colonnes[dossier] = largeur_max + 3

    noms_dossiers = list(colonnes.keys())
    
    # Affichage des en-têtes (noms des sous-dossiers)
    en_tetes = "".join(dossier.ljust(largeurs_colonnes[dossier]) for dossier in noms_dossiers)
    print(en_tetes)
    print("-" * len(en_tetes))

    # Affichage des fichiers ligne par ligne
    # zip_longest permet d'itérer jusqu'à la liste la plus longue
    lignes_fichiers = list(itertools.zip_longest(*colonnes.values(), fillvalue=""))
    
    for ligne in lignes_fichiers:
        ligne_formatee = ""
        for dossier, fichier in zip(noms_dossiers, ligne):
            ligne_formatee += fichier.ljust(largeurs_colonnes[dossier])
        print(ligne_formatee)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Affiche les fichiers des sous-dossiers en colonnes.")
    parser.add_argument("dossier", type=str, help="Chemin du dossier racine à analyser")
    args = parser.parse_args()
    
    afficher_colonnes_dossiers(args.dossier)