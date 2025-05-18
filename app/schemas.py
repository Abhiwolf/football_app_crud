from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AreaBase(BaseModel):
    name: str
    country_code: str


class Area(AreaBase):
    id: int

    class Config:
        orm_mode = True


class TeamBase(BaseModel):
    name: str
    founded: Optional[int]
    stadium: Optional[str]
    area_id: int


class Team(TeamBase):
    id: int

    class Config:
        orm_mode = True


class PlayerBase(BaseModel):
    name: str
    position: str
    nationality: str
    team_id: int


class Player(PlayerBase):
    id: int

    class Config:
        orm_mode = True


class MatchBase(BaseModel):
    match_date: datetime
    team_home_id: int
    team_away_id: int
    area_id: int


class Match(MatchBase):
    id: int

    class Config:
        orm_mode = True
