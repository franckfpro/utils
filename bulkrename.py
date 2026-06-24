#!/usr/bin/env python3
"""Un script pour renommer en masse les fichiers d'un dossier via Neovim."""

import argparse
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    """Gère les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(
        description="Renomme en masse les fichiers d'un dossier en utilisant Neovim."
    )
    parser.add_argument(
        "directory",
        type=str,
        help="Le chemin du dossier contenant les fichiers à renommer.",
    )
    return parser.parse_args()


def bulk_rename(directory_path: str) -> None:
    """Prend les fichiers d'un dossier, permet leur édition dans nvim,

    et applique les changements de nom.
    """
    target_dir = Path(directory_path).resolve()

    if not target_dir.is_dir():
        print(f"Erreur : '{target_dir}' n'est pas un dossier valide.", file=sys.stderr)
        sys.exit(1)

    # 1. Lister uniquement les fichiers (on ignore les dossiers pour plus de sécurité)
    # triés par ordre alphabétique pour la cohérence
    original_files = [f for f in target_dir.iterdir() if f.is_file()]

    if not original_files:
        print("Aucun fichier à renommer dans ce dossier.")
        return

    # Extraire uniquement les noms de fichiers pour l'édition
    original_names = [f.name for f in original_files]

    # 2. Créer un fichier temporaire contenant la liste des noms
    with tempfile.NamedTemporaryFile(mode="w+", suffix=".txt", delete=False) as temp_file:
        temp_file_path = Path(temp_file.name)
        temp_file.write("\n".join(original_names) + "\n")

    try:
        # 3. Ouvrir Neovim avec la liste des fichiers
        # On utilise ['nvim', ...] directement
        subprocess.run(["nvim", str(temp_file_path)], check=True)

        # 4. Lire les modifications apportées par l'utilisateur
        with open(temp_file_path, "r", encoding="utf-8") as file:
            edited_names = [line.strip() for line in file if line.strip()]

    finally:
        # Nettoyage du fichier temporaire, quoi qu'il arrive
        if temp_file_path.exists():
            temp_file_path.unlink()

    # 5. Validation des correspondances
    if len(original_names) != len(edited_names):
        print(
            f"Erreur : Le nombre de lignes a changé. "
            f"Attendu : {len(original_names)}, Reçu : {len(edited_names)}.\n"
            f"Opération annulée pour éviter les désynchronisations.",
            file=sys.stderr,
        )
        sys.exit(1)

    # 6. Application des renommages
    count = 0
    for old_file, new_name in zip(original_files, edited_names):
        if old_file.name == new_name:
            continue  # Aucune modification pour ce fichier

        new_file_path = old_file.with_name(new_name)

        # Sécurité : Éviter d'écraser un fichier existant accidentellement
        if new_file_path.exists():
            print(
                f"Attention : Impossible de renommer '{old_file.name}' en '{new_name}'. "
                f"Le fichier cible existe déjà.",
                file=sys.stderr,
            )
            continue

        try:
            old_file.rename(new_file_path)
            print(f"Renommé : '{old_file.name}' -> '{new_name}'")
            count += 1
        except OSError as e:
            print(
                f"Erreur lors du renommage de '{old_file.name}': {e}",
                file=sys.stderr,
            )

    print(f"\nOpération terminée. {count} fichier(s) renommé(s).")


def main() -> None:
    """Point d'entrée principal du script."""
    args = parse_arguments()
    bulk_rename(args.directory)


if __name__ == "__main__":
    main()
