# football_app_crud
It is backend application using python fastapi with PostgreSQL database,

# ⚽ Football Explorer API

A full-stack application backend built with FastAPI and PostgreSQL to explore football teams, players, matches, and areas.

## 🚀 Features
- List and filter matches, teams, players
- Query by area or team
- Swagger documentation at `/docs`
- Dockerized backend and PostgreSQL

## 📦 Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Swagger UI

## 📁 Project Structure
```
app/
├── crud.py
├── database.py
├── main.py
├── models.py
├── routers/
├── schemas.py
seed.py
Dockerfile
docker-compose.yml
requirements.txt
```

## 🛠 Setup Instructions

### 1. Clone the repository
```bash
git clone <your_repo_url>
cd <repo>
```

### 2. Build and start services
```bash
docker-compose up --build
```

### 3. Run seed data
```bash
docker exec -it <backend_container_id> python seed.py
```

### 4. Open API Docs
Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## ✅ API Endpoints
- `GET /matches` — List all matches
- `GET /teams` — List all teams
- `GET /players/{id}` — Get player info
- `GET /areas` — List all areas

## ⚙️ Environment
- DB user: `user`
- DB password: `pass`
- DB name: `football`

## 📌 Notes
- Filters via query params (e.g., `/teams?area=Spain`)
- Swagger for API testing and documentation
- Linting and testing setup recommended for production

---

## Run application 
- # uvicorn app.main:app --reload --host 0.0.0.0 --port 8000