def lire_gros_fichier(fichier):
    with open(fichier, "r") as f:
        for ligne in f:
            yield ligne.strip()

for ligne in lire_gros_fichier("gros_fichier.txt"):
    print(ligne)  # Traite une ligne à la fois, sans charger tout le fichier
