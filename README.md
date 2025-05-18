# football_app_crud
It is backend application using python fastapi with PostgreSQL database,

# Football Explorer API

A full-stack application backend built with FastAPI and PostgreSQL to explore football teams, players, matches, and areas.

## Features
- List and filter matches, teams, players
- Query by area or team
- Swagger documentation at `/docs`
- Dockerized backend and PostgreSQL

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Docker
- Swagger UI

## Project Structure
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

### 1. Clone the repository
```bash
git clone https://github.com/Abhiwolf/football_app_crud.git
```

### 2. Create python virtual env
```
create virtual env using .venv on vs code
```

### 3. Setup Instructions
```
 pip install -r requirements.txt
 ```

### 4. Run application 
- # uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

### 5. Add seed data into database
```
python seed.py - it will add some data into databse 
postgresql://postgres:mypassword@localhost:5432/football_db

```


### 6. Open API Docs
Visit [http://localhost:8000/docs](http://localhost:8000/docs)

## API Endpoints
- `GET /matches` — List all matches
- `GET /teams` — List all teams
- `GET /players/{id}` — Get player info
- `GET /areas` — List all areas

## Environment
- DB user: `postgres`
- DB password: `mypassword`
- DB name: `football_db`

## 📌 Notes
- Filters via query params (e.g., `/teams?area=Spain`)
- Swagger for API testing and documentation
- Linting and testing setup recommended for production

---
