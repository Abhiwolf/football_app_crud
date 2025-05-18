from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, database
from typing import List

router = APIRouter(prefix="/areas", tags=["areas"])


@router.get("/", response_model=List[schemas.Area])
def get_areas(db: Session = Depends(database.get_db)):
    return db.query(models.Area).all()
