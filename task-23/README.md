# Task 23 — Student Management System (Dockerized)

Also covers tasks 20, 21 and 22:

| Task | Where it is covered |
|------|---------------------|
| 20 — Frontend → FastAPI → PostgreSQL, 3 containers | `frontend` (nginx), `backend` (FastAPI), `db` (PostgreSQL) in `docker-compose.yml` |
| 21 — Health check | `GET /health` in `backend/main.py`; `healthcheck:` on `backend` and `db` in Compose |
| 22 — CRUD + data survives restarts | `/students` endpoints; named volume `postgres_data` |
| 23 — Full mini project | Everything in this folder |

## Architecture

```
Browser → frontend (nginx :8080) → /api/* → backend (FastAPI :8000) → db (PostgreSQL)
                    all on the sms-network Docker network
```

## Run

```bash
docker compose up --build
```

- UI: http://localhost:8080
- API docs (Swagger): http://localhost:8001/docs
- Health: http://localhost:8001/health

Configuration comes from `.env` (copy `.env.example` if it is missing).

## API

| Method | Path | Purpose |
|--------|------|---------|
| POST | `/students` | Create a student |
| GET | `/students` | List all students |
| GET | `/students?search=text` | Search name / email / course |
| GET | `/students/{id}` | View one student |
| PUT | `/students/{id}` | Update a student |
| DELETE | `/students/{id}` | Delete a student |
| GET | `/health` | Health check (checks DB connection) |

## Start-up order

`db` (healthy via `pg_isready`) → `backend` (healthy via `/health`) → `frontend`.

## Persistence test

```bash
docker compose down        # removes containers, keeps the volume
docker compose up -d
# students added earlier are still listed
docker compose down -v     # -v deletes the volume (data is lost)
```

## Notes

- The backend is published on host port 8001 because 8000 was in use by the task-19 container.
- The frontend reaches the backend through nginx (`/api/` → `http://backend:8000/`), so no CORS setup is needed.

## Screenshots

All are in [shots/](shots/).

| File | Shows |
|------|-------|
| `01-docker-compose-ps.png` | 3 containers running, network, volume, `/health` response |
| `02-frontend-ui.png` | Student Management UI at http://localhost:8080 |
| `03-swagger-docs.png` | FastAPI Swagger docs listing all endpoints |
| `04-health-endpoint.png` | `/health` in the browser |
| `05-api-search-get-delete.png` | Search, get, delete and 404 after delete |
| `06-persistence-after-restart.png` | Data still present after `docker compose down` and `up` |
