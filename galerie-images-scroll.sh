#!/bin/bash

# Script pour générer une page HTML avec des images en scrolling
# Utilisation: ./generate_image_gallery.sh [dossier_images]

# Dossier par défaut
IMAGE_DIR="${1:-.}"
OUTPUT_FILE="$(basename "$IMAGE_DIR").html"

# Vérifier que le dossier existe
if [ ! -d "$IMAGE_DIR" ]; then
    echo "Erreur: Le dossier '$IMAGE_DIR' n'existe pas."
    exit 1
fi

# Créer le fichier HTML
cat > "$OUTPUT_FILE" << 'HTML_HEADER'
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galerie d'images</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .gallery {
            max-width: 100%;
            margin: 0;
            padding: 0;
        }
        .gallery img {
            display: block;
            width: 1000px;
            height: auto;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
    <div class="gallery">
HTML_HEADER

# Ajouter les images au fichier HTML
find "$IMAGE_DIR" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.webp" \) | sort | while read -r image; do
    filename=$(basename "$image")
    escaped_filename=$(echo "$filename" | sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/"/\&quot;/g; s/'\''/\&apos;/g')
    echo "        <img src=\"$(echo "$image" | sed 's/ /%20/g')\" alt=\"$escaped_filename\" />" >> "$OUTPUT_FILE"
done

# Fermer le fichier HTML
cat >> "$OUTPUT_FILE" << 'HTML_FOOTER'
    </div>
</body>
</html>
HTML_FOOTER

echo "Page HTML générée: $OUTPUT_FILE"
echo "Nombre d'images ajoutées: $(find "$IMAGE_DIR" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.webp" \) | wc -l)"
