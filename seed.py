from sqlalchemy.orm import Session
from app import models, database
from datetime import datetime


def seed_data():
    db = next(database.get_db())

    area = models.Area(name="Spain", country_code="ES")
    db.add(area)
    db.commit()
    db.refresh(area)

    team1 = models.Team(name="FC Barcelona", founded=1899, stadium="Camp Nou", area_id=area.id)
    team2 = models.Team(name="Real Madrid", founded=1902, stadium="Santiago Bernabéu", area_id=area.id)
    db.add_all([team1, team2])
    db.commit()

    player1 = models.Player(name="Lionel Messi", position="Forward", nationality="Argentina", team_id=team1.id)
    player2 = models.Player(name="Karim Benzema", position="Forward", nationality="France", team_id=team2.id)
    db.add_all([player1, player2])
    db.commit()

    match = models.Match(
        match_date=datetime(2025, 6, 1, 20, 0),
        team_home_id=team1.id,
        team_away_id=team2.id,
        area_id=area.id
    )
    db.add(match)
    db.commit()

    print("✅ Seed data inserted successfully.")


if __name__ == '__main__':
    seed_data()
