from fastapi import FastAPI
from .routers import matches, teams, players, areas
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(matches.router)
app.include_router(teams.router)
app.include_router(players.router)
app.include_router(areas.router)
