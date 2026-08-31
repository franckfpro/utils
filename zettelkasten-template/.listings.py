import os

def generer_references_internes():
    dossier = os.getcwd()  # Prend le dossier courant
    with open("ressources-internes.md", "w", encoding="utf-8") as f:
        f.write("| lien | zettel |\n")
        f.write("|------|--------|\n")

        for racine, dossiers, fichiers in os.walk(dossier):
            # Ignorer les dossiers commençant par .
            dossiers[:] = [d for d in dossiers if not d.startswith('.')]

            for fichier in fichiers:
                nom, extension = os.path.splitext(fichier)
                chemin_relatif = os.path.relpath(os.path.join(racine, fichier), start=dossier)

                if extension.lower() == '.md':
                    ligne = f"| [{nom}]({chemin_relatif}) | [[{nom}]] |\n"
                elif extension.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.pdf'):
                    ligne = f"| [{fichier}]({chemin_relatif}) | ![[{nom}]] |\n"
                else:
                    continue  # Ignorer les autres types de fichiers

                f.write(ligne)

if __name__ == "__main__":
    generer_references_internes()
    print("Fichier ressources-internes.md généré avec succès dans le dossier courant !")
