'''
pip install plyvel

Utilisation
1. Cas de base (clé + valeur, binaire encodé en base64) :
python leveldb_to_csv.py /chemin/vers/ma_leveldb output.csv
2. Avec un délimiteur personnalisé (TSV) :
python leveldb_to_csv.py /chemin/vers/ma_leveldb output.tsv --delimiter $'\t'
3. Ignorer les valeurs binaires :
python leveldb_to_csv.py /chemin/vers/ma_leveldb output.csv --no-binary
4. Extraire uniquement les clés :
python leveldb_to_csv.py /chemin/vers/ma_leveldb cles.csv --keys-only
5. Extraire uniquement les valeurs :
python leveldb_to_csv.py /chemin/vers/ma_leveldb valeurs.csv --values-only
'''

#!/usr/bin/env python3
"""
Convertit une base LevelDB en CSV.
Chaque ligne du CSV contient : clé,valeur (encodées en UTF-8 ou base64 si binaire).
"""

import argparse
import base64
import csv
import os
import sys
from pathlib import Path

import plyvel

def is_binary(data: bytes) -> bool:
    """Vérifie si des données sont probablement binaires."""
    try:
        data.decode("utf-8")
        return False
    except UnicodeDecodeError:
        return True

def encode_value(data: bytes) -> str:
    """Encode une valeur en UTF-8 ou base64 si binaire."""
    if is_binary(data):
        return base64.b64encode(data).decode("ascii")
    return data.decode("utf-8")

def leveldb_to_csv(
    db_path: str,
    output_csv: str,
    delimiter: str = ",",
    include_binary: bool = True,
    keys_only: bool = False,
    values_only: bool = False,
) -> None:
    """
    Convertit une base LevelDB en CSV.

    Args:
        db_path: Chemin vers le dossier de la base LevelDB.
        output_csv: Chemin du fichier CSV de sortie.
        delimiter: Délimiteur CSV (par défaut ',').
        include_binary: Si True, les valeurs binaires sont encodées en base64.
        keys_only: Si True, n'écrit que les clés.
        values_only: Si True, n'écrit que les valeurs.
    """
    if not os.path.isdir(db_path):
        print(f"Erreur : '{db_path}' n'est pas un dossier LevelDB valide.", file=sys.stderr)
        sys.exit(1)

    try:
        db = plyvel.DB(db_path)
    except Exception as e:
        print(f"Erreur lors de l'ouverture de la base LevelDB : {e}", file=sys.stderr)
        sys.exit(1)

    headers = []
    if not keys_only:
        headers.append("clé")
    if not values_only:
        headers.append("valeur")

    row_count = 0
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        if headers:
            writer.writerow(headers)

        for key, value in db:
            row = []
            if not keys_only:
                row.append(encode_value(key))
            if not values_only:
                if include_binary:
                    row.append(encode_value(value))
                else:
                    try:
                        row.append(value.decode("utf-8"))
                    except UnicodeDecodeError:
                        continue  # Ignore les valeurs binaires
            writer.writerow(row)
            row_count += 1

    print(f"Conversion terminée : {output_csv} ({row_count} lignes écrites).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convertit une base LevelDB en CSV.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("db_path", help="Chemin vers le dossier de la base LevelDB")
    parser.add_argument("output_csv", help="Fichier CSV de sortie")
    parser.add_argument(
        "--delimiter",
        default=",",
        help="Délimiteur CSV (ex: ';' ou '\\t' pour TSV)",
    )
    parser.add_argument(
        "--no-binary",
        action="store_true",
        help="Ignore les valeurs binaires (au lieu de les encoder en base64)",
    )
    parser.add_argument(
        "--keys-only",
        action="store_true",
        help="N'écrire que les clés dans le CSV",
    )
    parser.add_argument(
        "--values-only",
        action="store_true",
        help="N'écrire que les valeurs dans le CSV",
    )
    args = parser.parse_args()

    leveldb_to_csv(
        db_path=args.db_path,
        output_csv=args.output_csv,
        delimiter=args.delimiter,
        include_binary=not args.no_binary,
        keys_only=args.keys_only,
        values_only=args.values_only,
    )
