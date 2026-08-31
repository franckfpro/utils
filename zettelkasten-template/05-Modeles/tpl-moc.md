---
id: {{date:YYYYMMDDHHmm}}
type: moc
tags:
  - moc
  - domaine/sujet
date_creation: {{date:YYYY-MM-DD}}
---

# MOC - {{title}}

## Vision globale et Synthèse
<!-- Résumé structuré de la thématique couverte par cette carte de contenu. -->

## Structure du domaine

### 1. Fondations et Notions de base
- [[NotePermanente1]]
- [[NotePermanente2]]

### 2. Implémentations et Pratiques
- [[NotePermanente3]]
- [[NotePermanente4]]

## Projets associés
- [[Projet - Implémentation]]

## Index dynamique (Dataview)
```dataview
LIST FROM #domaine/sujet
WHERE file.name != this.file.name
SORT file.mtime DESC

```

