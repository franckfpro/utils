from fastapi import FastAPI

from app.database import Base, engine
from app.routers import users

# Création des tables à la volée pour la démo (En prod, on préférera Alembic)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Utilisateurs - Démo Éducative",
    description="Un exemple de CRUD complet respectant les standards Python.",
    version="1.0.0",
)

# Inclusion des routes
app.include_router(users.router)


@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API de démonstration. Allez sur /docs"}
