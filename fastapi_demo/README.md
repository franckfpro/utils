# FastAPI CRUD Demonstration & Architecture

Ce projet est une vitrine pédagogique démontrant la mise en œuvre d'une architecture de production moderne, modulaire et respectant les standards Python (**PEP 8**, **PEP 517**) avec le framework **FastAPI**.

L'application expose une API REST complète (CRUD) interagissant avec une table `utilisateurs` stockée dans une base de données **SQLite3**.

## Installation et lancement

```
# Créer et activer l'environnement virtuel
python3 -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Mettre à jour pip
pip install --upgrade pip

pip install -r requirements.txt

uv run uvicorn app.main:app --reload
#Accès à la documentation interactive : http://127.0.0.1:8000/docs

pytest -v
```

---

## 📁 Architecture du Projet

Le projet applique une séparation stricte des responsabilités (Modèles, Couche d'accès aux données (CRUD), Schémas de validation, et Routes) :

```text
fastapi_demo/
├── app/
│   ├── __init__.py
│   ├── main.py           # Point d'entrée de l'application et init FastAPI
│   ├── config.py         # Configuration globale (Pydantic Settings)
│   ├── database.py       # Configuration SQLAlchemy (Engine, SessionLocal)
│   ├── models.py         # Modèles de tables ORM (SQLAlchemy)
│   ├── schemas.py        # Modèles de validation de données (Pydantic)
│   ├── crud.py           # Opérations d'accès à la base de données
│   └── routers/
│       ├── __init__.py
│       └── users.py      # Endpoints REST pour la ressource 'utilisateurs'
├── tests/
│   ├── __init__.py
│   ├── conftest.py       # Fixtures Pytest (Base de données isolée et client de test)
│   └── test_users.py     # Tests d'intégration du CRUD
├── requirements.txt      # Dépendances du projet
└── README.md             # Documentation
