import random

def tirer_une_carte():
    couleurs = ["Pique", "Cœur", "Carreau", "Trèfle"]
    valeurs = ["As", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi"]

    # random.choice gère la distribution uniforme automatiquement
    couleur_tiree = random.choice(couleurs)
    valeur_tiree = random.choice(valeurs)

    return f"{valeur_tiree} de {couleur_tiree}"

# Exemple d'exécution
print(tirer_une_carte())