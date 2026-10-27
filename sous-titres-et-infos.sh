#!/usr/bin/env bash

shopt -s nullglob nocaseglob

for fichier in *.mp4; do
  [[ -f "$fichier" ]] || continue

  base="${fichier%.*}"
  sortie="${base}.txt"
  temporaire="$(mktemp)"

  # Repartir d'un fichier vide si le script a déjà été exécuté
  : > "$sortie"

  echo "Traitement : $fichier"

  nb_pistes=$(ffprobe -v error \
    -select_streams s \
    -show_entries stream=index \
    -of csv=p=0 "$fichier" | wc -l)

  for (( piste=0; piste<nb_pistes; piste++ )); do
    if ffmpeg -y -v error -i "$fichier" \
      -map "0:s:$piste" -c:s srt \
      -f srt "$temporaire"; then
      {
        printf '\n===== Piste de sous-titres %d =====\n' "$piste"
        cat "$temporaire"
      } >> "$sortie"
    else
      echo "Échec de l'extraction de la piste $piste : $fichier" >&2
    fi
  done

  {
    printf '\n\n===== Métadonnées ffprobe =====\n'
    ffprobe -v error -show_format -show_streams "$fichier"
  } >> "$sortie"

  rm -f "$temporaire"
done

