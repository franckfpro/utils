import numpy as np
import pandas as pd

# 1. Approche Matricielle (Tensorielle) avec NumPy
# Configuration : 2 ans (2) x 4 magasins (4) x 3 produits (3)
# On génère des ventes aléatoires entre 10 et 100 unités
np.random.seed(42)  # Pour avoir les mêmes résultats
ventes_3d = np.random.randint(10, 100, size=(2, 4, 3))

print("Forme du tenseur (Années, Magasins, Produits) :", ventes_3d.shape)
print("\nDonnées de l'Année 1 (Index 0) :\n", ventes_3d[0])

print("-" * 50)

# 2. Approche Tabulaire avec Pandas (MultiIndex / Format Long)
# En Data Science, on préfère souvent "aplatir" ces dimensions pour l'analyse
annees = ['2025', '2026']
magasins = ['Paris', 'Lyon', 'Marseille', 'Lille']
produits = ['Smartphone', 'Ordinateur', 'Tablette']

# Création d'un index multidimensionnel (MultiIndex)
index = pd.MultiIndex.from_product([annees, magasins, produits], 
                                   names=['Année', 'Magasin', 'Produit'])

# Aplatissement de notre cube NumPy pour le mettre dans le DataFrame
df = pd.DataFrame(ventes_3d.flatten(), index=index, columns=['Unités Vendues'])

# Affichage des premières lignes
print("\nVue sous forme de DataFrame multidimensionnel :")
print(df.head(12))
print(df.xs(('2026', 'Smartphone'), level=('Année', 'Produit')))
