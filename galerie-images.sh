#!/bin/bash

# Script pour créer une page HTML avec les images d'un dossier

# Vérifier qu'un dossier est fourni
if [ $# -eq 0 ]; then
    echo "Usage: $0 <dossier_contenant_les_images> [fichier_html_de_sortie]"
    echo "Exemple: $0 mes_images galerie.html"
    exit 1
fi

DOSSIER="$1"
FICHIER_HTML="${2:-galerie.html}"

# Vérifier que le dossier existe
if [ ! -d "$DOSSIER" ]; then
    echo "Erreur: Le dossier '$DOSSIER' n'existe pas."
    exit 1
fi

# Créer le fichier HTML
cat > "$FICHIER_HTML" <<EOF
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Galerie d'images - $(basename "$DOSSIER")</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .gallery img {
            width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        .gallery img:hover {
            transform: scale(1.05);
        }
        .image-container {
            background: white;
            padding: 10px;
            border-radius: 8px;
        }
        .image-name {
            text-align: center;
            margin-top: 10px;
            font-size: 14px;
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Galerie d'images - $(basename "$DOSSIER")</h1>
    <div class="gallery">
EOF

# Ajouter chaque image au fichier HTML
find "$DOSSIER" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.webp" -o -iname "*.svg" \) | sort | while read -r image; do
    nom_fichier=$(basename "$image")
    cat >> "$FICHIER_HTML" <<EOF
        <div class="image-container">
            <img src="$image" alt="$nom_fichier">
            <div class="image-name">$nom_fichier</div>
        </div>
EOF
done

# Fermer le fichier HTML
cat >> "$FICHIER_HTML" <<EOF
    </div>
</body>
</html>
EOF

# Compter le nombre d'images
NB_IMAGES=$(find "$DOSSIER" -maxdepth 1 -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.webp" -o -iname "*.svg" \) | wc -l)

echo "Page HTML générée: $FICHIER_HTML ($NB_IMAGES images trouvées)"
