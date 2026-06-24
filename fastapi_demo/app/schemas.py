from typing import Optional
from pydantic import BaseModel, EmailStr


# Propriétés communes à la création et à la lecture
class UserBase(BaseModel):
    utilisateur: str
    email: EmailStr
    completement: Optional[str] = None


# Schéma pour la création (Données requises en entrée)
class UserCreate(UserBase):
    pass


# Schéma pour la mise à jour (Tout est optionnel pour du PATCH propre)
class UserUpdate(BaseModel):
    utilisateur: Optional[str] = None
    email: Optional[EmailStr] = None
    completement: Optional[str] = None


# Schéma retourné par l'API (Inclusion de l'ID)
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
