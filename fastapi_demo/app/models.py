from sqlalchemy import Column, Integer, String
from app.database import Base


class UserModel(Base):
    __tablename__ = "utilisateurs"

    id = Column(Integer, primary_key=True, index=True)
    utilisateur = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    completement = Column(String, nullable=True)
