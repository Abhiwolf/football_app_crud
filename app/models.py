from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base


class Area(Base):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country_code = Column(String)
    teams = relationship("Team", back_populates="area")
    matches = relationship("Match", back_populates="area")


class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    founded = Column(Integer)
    stadium = Column(String)
    area_id = Column(Integer, ForeignKey("areas.id"))
    area = relationship("Area", back_populates="teams")
    players = relationship("Player", back_populates="team")
    home_matches = relationship(
        "Match",
        back_populates="home_team",
        foreign_keys="Match.team_home_id"
    )
    away_matches = relationship(
        "Match",
        back_populates="away_team",
        foreign_keys="Match.team_away_id"
    )


class Player(Base):
    __tablename__ = "players"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    position = Column(String)
    nationality = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="players")


class Match(Base):
    __tablename__ = "matches"
    id = Column(Integer, primary_key=True, index=True)
    match_date = Column(DateTime)
    team_home_id = Column(Integer, ForeignKey("teams.id"))
    team_away_id = Column(Integer, ForeignKey("teams.id"))
    area_id = Column(Integer, ForeignKey("areas.id"))
    home_team = relationship(
        "Team",
        foreign_keys=[team_home_id],
        back_populates="home_matches"
    )
    away_team = relationship(
        "Team",
        foreign_keys=[team_away_id],
        back_populates="away_matches"
    )
    area = relationship("Area", back_populates="matches")
