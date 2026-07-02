#!/bin/bash

# Arrêt du script en cas d'erreur
set -e

PROJECT_DIR="stoic_tasks"
echo "Création du projet $PROJECT_DIR..."

# Création du répertoire et initialisation de uv
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"
uv init
uv add django

# Initialisation du projet Django et de l'application
uv run django-admin startproject config .
uv run python manage.py startapp tasks

# Création de l'arborescence des templates
mkdir -p tasks/templates/tasks
mkdir -p templates

echo "Architecture créée avec succès. Prêt pour l'intégration des fichiers."