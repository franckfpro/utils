#!/usr/bin/env python3
"""
Script pour afficher un élément aléatoire d'une liste de dictionnaires depuis un fichier JSON.
"""

import argparse
import json
import random
from tabulate import tabulate

def load_json_file(file_path: str) -> list[dict]:
    """Charge et retourne le contenu d'un fichier JSON."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list):
            raise ValueError("Le fichier JSON doit contenir une liste de dictionnaires.")
        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Chaque élément de la liste doit être un dictionnaire.")
        return data
    except FileNotFoundError:
        raise FileNotFoundError(f"Le fichier {file_path} n'existe pas.")
    except json.JSONDecodeError:
        raise ValueError(f"Le fichier {file_path} n'est pas un JSON valide.")

def display_random_item(data: list[dict]) -> None:
    """Affiche un élément aléatoire de la liste sous forme de tableau."""
    if not data:
        print("La liste est vide.")
        return
    item = random.choice(data)
    headers = list(item.keys())
    values = [item[key] for key in headers]
    print(tabulate([values], headers=headers, tablefmt="heavy_grid"))

def main() -> None:
    """Point d'entrée principal du script."""
    parser = argparse.ArgumentParser(
        description="Affiche un élément aléatoire d'une liste de dictionnaires depuis un fichier JSON."
    )
    parser.add_argument(
        "json_file",
        type=str,
        help="Chemin vers le fichier JSON contenant une liste de dictionnaires."
    )
    args = parser.parse_args()

    try:
        data = load_json_file(args.json_file)
        display_random_item(data)
    except (ValueError, FileNotFoundError) as e:
        print(f"Erreur : {e}")

if __name__ == "__main__":
    main()
