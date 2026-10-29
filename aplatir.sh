#!/usr/bin/env bash

racine="${1:-.}"

find "$racine" -mindepth 2 -maxdepth 2 -type f -print0 |
while IFS= read -r -d '' fichier; do
    sous_dossier=$(basename "$(dirname "$fichier")")
    nom_fichier=$(basename "$fichier")
    destination="$racine/${sous_dossier}_${nom_fichier}"

    if [[ -e "$destination" || -L "$destination" ]]; then
        printf 'Ignoré (destination déjà existante) : %s\n' "$destination" >&2
        continue
    fi

    mv -- "$fichier" "$destination"
done
