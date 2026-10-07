# Task 10 - Run FastAPI Using a Different Host Port

## Objective

Run the same `super30-api` Docker image using a different host port.

The FastAPI application continues to run on port 8000 inside the Docker container, but it is made accessible through port 5000 on the host machine.

---

## Prerequisites

- Docker Desktop installed and running
- `super30-api` Docker image created
- FastAPI application available
- Task 9 completed

---

## Step 1 - Verify Docker Image

Run:

```powershell
docker images