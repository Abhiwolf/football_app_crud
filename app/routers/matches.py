from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database
from typing import List

router = APIRouter(prefix="/matches", tags=["matches"])


@router.get("/", response_model=List[schemas.Match])
def get_matches(area_id: int = None, db: Session = Depends(database.get_db)):
    query = db.query(models.Match)
    if area_id:
        query = query.filter(models.Match.area_id == area_id)
    return query.all()