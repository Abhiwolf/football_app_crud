from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(prefix="/players", tags=["players"])


@router.get("/{player_id}", response_model=schemas.Player)
def get_player(player_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Player).filter(models.Player.id == player_id).first()
