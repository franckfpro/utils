libreoffice --headless --convert-to pdf $1

google-chrome --headless --print-to-pdf="sortie.pdf" \
  --timeout=5000 "https://exemple.com"

google-chrome --headless \
  --print-to-pdf="$PWD/sortie.pdf" \
  "file://$PWD/page.html"

