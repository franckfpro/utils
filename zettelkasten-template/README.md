```text
📂 Projet-Zettelkasten
├── 📁 00-Boite-de-reception
├── 📁 01-Notes-permanentes
├── 📁 02-Notes-de-reference
├── 📁 03-Index-et-MOC
├── 📁 04-Projets-actifs
├── 📁 05-Modeles
├── 📁 06-Pieces-jointes
└── 📁 07-Kanban
    ├── 📁 07-01-A-Faire
    ├── 📁 07-02-En-Cours
    ├── 📁 07-03-A-Valider
    └── 📁 07-04-Termine

```

**00-Boite-de-reception (Inbox)**

* **Concept**: L'entonnoir de capture. Toute nouvelle idée, lien, bout de code ou pensée brute atterrit ici avant traitement.
* **Fonctionnement**: Cet espace doit être vidé et trié régulièrement. Les notes sont ensuite transformées, supprimées ou classées.

**01-Notes-permanentes (Le Zettelkasten)**

* **Concept**: Le cœur de la base de connaissances. Cet espace contient les notes atomiques, rédigées avec tes propres mots, où une note correspond à une idée unique.
* **Fonctionnement**: Chaque fichier utilise un identifiant unique (comme l'horodatage) et un réseau de liens bidirectionnels pour se connecter aux autres concepts.

**02-Notes-de-reference (Littérature)**

* **Concept**: Les résumés et extraits issus de ta consommation d'information externe (documentation technique, articles, livres, tutoriels vidéo).
* **Fonctionnement**: Une note par source. Ces notes servent de matière première pour créer ensuite tes propres notes permanentes.

**03-Index-et-MOC (Maps of Content)**

* **Concept**: Les tables des matières thématiques de ta base de données. L'approche Zettelkasten étant "plate", les MOC permettent de structurer la pensée par le haut.
* **Fonctionnement**: Ce sont des notes qui agissent comme des carrefours, regroupant et organisant les liens vers de multiples notes permanentes autour d'un sujet précis (ex: `[[MOC - Architecture Docker]]`).

**04-Projets-actifs**

* **Concept**: L'espace orienté vers l'action, isolé du stockage de connaissances pures.
* **Fonctionnement**: Ce dossier accueille tes fichiers liés à des livrables en cours de réalisation. C'est ici que tu places les tickets Kanban générés avec le template précédent, tes brouillons et tes jalons d'avancement. Une fois le projet terminé, les fichiers peuvent être archivés.

**05-Modeles (Templates)**

* **Concept**: Le dossier système regroupant l'ensemble de tes moules de création.
* **Fonctionnement**: Contient les fichiers Markdown pré-remplis (modèle de note permanente, modèle de Kanban, modèle de MOC) utilisés par ton logiciel (comme les plugins Obsidian) pour instancier de nouvelles notes avec la bonne structure YAML.

**06-Pieces-jointes (Assets)**

* **Concept**: Le stockage des médias et fichiers non-Markdown.
* **Fonctionnement**: Centralise toutes les images, schémas, fichiers PDF et autres documents attachés. Isoler ces fichiers permet de garder les dossiers de notes textuelles propres et facilite les recherches.

---

Dans Obsidian:

1. **Configurer le dossier des pièces jointes:**
1. Ouvre les paramètres d'Obsidian (l'icône d'engrenage en bas à gauche).
2. Va dans l'onglet **Fichiers et liens**.
3. Cherche l'option **Emplacement par défaut des nouvelles pièces jointes**.
4. Sélectionne **Dans le dossier spécifié ci-dessous**.
5. Dans le champ qui apparaît, choisis ton dossier: `06-Pieces-jointes`.

Désormais, toute image collée ou tout fichier glissé-déposé dans une note sera automatiquement rangé dans ce dossier, gardant ta racine propre.

2. **Activer le plugin natif des modèles:**
1. Reste dans les paramètres et sélectionne l'onglet **Plugins principaux**.
2. Fais défiler la liste jusqu'à l'option **Modèles**.
3. Active l'interrupteur associé.

3. **Configurer le dossier des modèles:**
1. Toujours dans les paramètres, descends dans le menu latéral gauche jusqu'à la section *Options des plugins* et clique sur **Modèles**.
2. Dans le champ **Emplacement du dossier des modèles**, sélectionne: `05-Modeles`.
3. Dans le champ **Format de la date**, saisis: `YYYY-MM-DD` (pour que tes variables `{{date:YYYY-MM-DD}}` fonctionnent).
4. Dans le champ **Format de l'heure**, saisis: `HH:mm`.

4. **Insérer un modèle dans une note:**
1. Crée une nouvelle note vide.
2. Ouvre la palette de commandes (Ctrl+P ou Cmd+P).
3. Tape et sélectionne **Modèles: Insérer un modèle**.
4. Choisis le modèle de ticket Kanban créé précédemment. Obsidian remplira automatiquement les champs de date et l'identifiant.

