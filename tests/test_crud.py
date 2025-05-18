import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import models, crud, database
from datetime import datetime

# Use an in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def test_db():
    database.Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()

    area = models.Area(name="Testland", country_code="TL")
    db.add(area)
    db.commit()
    db.refresh(area)

    team = models.Team(name="Test FC", founded=2000, stadium="Test Arena", area_id=area.id)
    db.add(team)
    db.commit()
    db.refresh(team)

    player = models.Player(name="Test Player", position="Midfielder", nationality="Testian", team_id=team.id)
    db.add(player)
    db.commit()
    db.refresh(player)

    match = models.Match(
        match_date=datetime(2030, 1, 1, 18, 0),
        team_home_id=team.id,
        team_away_id=team.id,
        area_id=area.id
    )
    db.add(match)
    db.commit()

    yield db

    db.close()
    database.Base.metadata.drop_all(bind=engine)


def test_get_all_areas(test_db):
    areas = crud.get_all_areas(test_db)
    assert len(areas) == 1
    assert areas[0].name == "Testland"


def test_get_area_by_name(test_db):
    area = crud.get_area_by_name(test_db, "Testland")
    assert area is not None
    assert area.country_code == "TL"


def test_get_teams(test_db):
    teams = crud.get_teams(test_db, area_name="Testland")
    assert len(teams) == 1
    assert teams[0].name == "Test FC"


def test_get_matches(test_db):
    matches = crud.get_matches(test_db)
    assert len(matches) == 1
    assert matches[0].team_home_id == matches[0].team_away_id


def test_get_player_by_id(test_db):
    player = crud.get_player_by_id(test_db, 1)
    assert player is not None
    assert player.name == "Test Player"
