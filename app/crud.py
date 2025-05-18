from sqlalchemy.orm import Session
from . import models, schemas


def get_all_areas(db: Session):
    return db.query(models.Area).all()


def get_area_by_name(db: Session, name: str):
    return db.query(models.Area).filter(models.Area.name == name).first()


def get_teams(db: Session, area_name: str = None):
    query = db.query(models.Team)
    if area_name:
        query = query.join(models.Area).filter(models.Area.name.ilike(f"%{area_name}%"))
    return query.all()


def get_matches(db: Session, area_id: int = None):
    query = db.query(models.Match)
    if area_id:
        query = query.filter(models.Match.area_id == area_id)
    return query.all()


def get_player_by_id(db: Session, player_id: int):
    return db.query(models.Player).filter(models.Player.id == player_id).first()