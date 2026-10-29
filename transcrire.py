'''
sudo apt update
sudo apt install ffmpeg python3-venv
mkdir -p ~/transcription
cd ~/transcription
python3 -m venv .venv
source .venv/bin/activate
pip install faster-whisper
'''
from faster_whisper import WhisperModel

fichier = "audio.mp3"  # Remplacez par le chemin de votre fichier
modele = WhisperModel("small", device="cpu", compute_type="int8")

segments, _ = modele.transcribe(fichier, language="fr")

with open("transcription.txt", "w", encoding="utf-8") as sortie:
    for segment in segments:
        sortie.write(segment.text.strip() + "\n")

print("Transcription enregistrée dans transcription.txt")

'''
Le fichier texte sera créé dans le dossier courant. Pour une meilleure précision, remplacez "small" par "medium" (plus lent et plus gourmand en mémoire) ; pour privilégier la vitesse, essayez "base". Fermez l’environnement virtuel avec deactivate quand vous avez terminé. Le paquet et son utilisation par Python sont documentés par le projet faster-whisper.

https://github.com/SYSTRAN/faster-whisper

alternatives:
    - https://flathub.org/en/apps/io.github.chidiwilliams.Buzz
    - https://flathub.org/en/apps/io.github.juergenfleiss.aTrain
'''
