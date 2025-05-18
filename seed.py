from sqlalchemy.orm import Session
from app import models, database
from datetime import datetime


def seed_data():
    db = next(database.get_db())

    # Create areas
    spain = models.Area(name="Spain", country_code="ES")
    england = models.Area(name="England", country_code="GB")
    germany = models.Area(name="Germany", country_code="DE")
    db.add_all([spain, england, germany])
    db.commit()

    # Create teams
    barca = models.Team(name="FC Barcelona", founded=1899, stadium="Camp Nou", area_id=spain.id)
    madrid = models.Team(name="Real Madrid", founded=1902, stadium="Santiago Bernabéu", area_id=spain.id)
    united = models.Team(name="Manchester United", founded=1878, stadium="Old Trafford", area_id=england.id)
    bayern = models.Team(name="Bayern Munich", founded=1900, stadium="Allianz Arena", area_id=germany.id)
    db.add_all([barca, madrid, united, bayern])
    db.commit()

    # Create players
    messi = models.Player(name="Lionel Messi", position="Forward", nationality="Argentina", team_id=barca.id)
    benzema = models.Player(name="Karim Benzema", position="Forward", nationality="France", team_id=madrid.id)
    rashford = models.Player(name="Marcus Rashford", position="Forward", nationality="England", team_id=united.id)
    neuer = models.Player(name="Manuel Neuer", position="Goalkeeper", nationality="Germany", team_id=bayern.id)
    db.add_all([messi, benzema, rashford, neuer])
    db.commit()

    # Create matches
    match1 = models.Match(match_date=datetime(2025, 6, 1, 20, 0), team_home_id=barca.id, team_away_id=madrid.id, area_id=spain.id)
    match2 = models.Match(match_date=datetime(2025, 6, 15, 18, 0), team_home_id=united.id, team_away_id=bayern.id, area_id=england.id)
    match3 = models.Match(match_date=datetime(2025, 7, 10, 21, 0), team_home_id=bayern.id, team_away_id=barca.id, area_id=germany.id)
    db.add_all([match1, match2, match3])
    db.commit()

    print("✅ Extended seed data inserted successfully.")


if __name__ == '__main__':
    seed_data()
