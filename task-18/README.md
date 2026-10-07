
---

# Task 18 — `README.md`

```markdown
# Task 18 — FastAPI Connected to PostgreSQL

## Objective

Create a FastAPI application that connects to a PostgreSQL database running in a separate Docker container.

The two applications run independently:

1. FastAPI container
2. PostgreSQL container

## Architecture

```text
┌──────────────────────┐
│   FastAPI Container  │
│      Port 8000       │
└──────────┬───────────┘
           │
           │ PostgreSQL
           ▼
┌──────────────────────┐
│ PostgreSQL Container │
│      Port 5432       │
└──────────────────────┘