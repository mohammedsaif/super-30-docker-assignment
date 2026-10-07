# 🐳 Super30 Docker Assignment

A complete hands-on Docker assignment covering **23 exercises**, starting from basic Docker containers and progressing to a complete **Student Management System** using Docker Compose, FastAPI, PostgreSQL, persistent volumes, networking, environment variables, and a frontend.

---

## 📌 Project Objective

The objective of this project is to demonstrate practical knowledge of:

- Docker Images
- Docker Containers
- Docker Hub
- Dockerfile
- Docker Build
- Port Mapping
- Environment Variables
- `.env` Configuration
- Docker Volumes
- Docker Networks
- PostgreSQL with Docker
- FastAPI
- Docker Compose
- Health Checks
- CRUD APIs
- Persistent Database Storage
- Three-Tier Architecture

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Docker Compose | Multi-container orchestration |
| Python | Application development |
| FastAPI | Backend REST API |
| PostgreSQL | Relational database |
| HTML / JavaScript | Frontend |
| Git / GitHub | Version control |

---

# 📂 Project Structure

```text
super30-docker-assignment/
├── README.md
├── .gitignore
├── task-01-ubuntu/      # Run Ubuntu container
├── task-02/             # Pull images / Python container
├── task-03/             # Custom container
├── task-04/             # Container lifecycle
├── task-05/             # Docker images
├── task-06/             # Python Dockerfile
├── task-07/             # Custom Python image
├── task-08/             # FastAPI in Docker
├── task-09/             # FastAPI on port 8000
├── task-10/             # Port mapping
├── task-11/             # Dockerfile instructions
├── task-12-13/          # requirements.txt + environment variable
├── task-14/             # .env file
├── task-15/             # Volumes
├── task-16/             # Networking
├── task-17/             # PostgreSQL container
├── task-18/             # FastAPI + PostgreSQL
├── task-19/             # Docker Compose: FastAPI + PostgreSQL
└── task-23/             # Student Management System (final project)
    ├── frontend/
    ├── backend/
    ├── shots/
    ├── .env.example
    ├── docker-compose.yml
    └── README.md
```

> Tasks 20–22 (three-tier, health check, CRUD) are combined into the final project in `task-23`.

---

## 🔐 Git Notes

- `.env` files are ignored via `.gitignore`; copy `.env.example` to `.env` in each task before running.
- Python caches, virtual environments, logs and local DB data are also ignored.

## ▶️ Quick Start (final project)

```bash
cd task-23
cp .env.example .env
docker compose up --build
```
