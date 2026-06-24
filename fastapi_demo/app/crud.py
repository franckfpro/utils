from typing import List, Optional
from sqlalchemy.orm import Session
from app import models, schemas


def get_user_by_id(db: Session, user_id: int) -> Optional[models.UserModel]:
    return (
        db.query(models.UserModel)
        .filter(models.UserModel.id == user_id)
        .first()
    )


def get_user_by_username(
    db: Session, username: str
) -> Optional[models.UserModel]:
    return (
        db.query(models.UserModel)
        .filter(models.UserModel.utilisateur == username)
        .first()
    )


def get_users(
    db: Session, skip: int = 0, limit: int = 100
) -> List[models.UserModel]:
    return db.query(models.UserModel).offset(skip).limit(limit).all()


def create_user(
    db: Session, user: schemas.UserCreate
) -> models.UserModel:
    db_user = models.UserModel(
        utilisateur=user.utilisateur,
        email=user.email,
        completement=user.completement,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(
    db: Session, db_user: models.UserModel, user_update: schemas.UserUpdate
) -> models.UserModel:
    update_data = user_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, db_user: models.UserModel) -> None:
    db.delete(db_user)
    db.commit()
