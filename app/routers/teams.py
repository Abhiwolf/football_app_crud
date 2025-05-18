from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database
from typing import List

router = APIRouter(prefix="/teams", tags=["teams"])

@router.get("/", response_model=List[schemas.Team])
def get_teams(area: str = None, db: Session = Depends(database.get_db)):
    query = db.query(models.Team)
    if area:
        query = query.join(models.Area).filter(models.Area.name.ilike(f"%{area}%"))
    return query.all()
