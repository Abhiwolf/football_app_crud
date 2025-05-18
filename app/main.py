from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import matches, teams, players, areas
from .database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow frontend (localhost:3000) to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(matches.router)
app.include_router(teams.router)
app.include_router(players.router)
app.include_router(areas.router)
