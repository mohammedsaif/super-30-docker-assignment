Create a requirements.txt containing FastAPI, Uvicorn, and other required dependencies. Install them automatically while building the Docker image.
Pass an environment variable to a Docker container and access its value from your Python/FastAPI application.
# Docker Tasks 12 & 13 — Dependencies and Environment Variables

## Objective

This project demonstrates:

- Creating a `requirements.txt` file for Python dependencies.
- Automatically installing dependencies while building a Docker image.
- Passing environment variables to a Docker container.
- Accessing environment variables from a FastAPI application.

---

## Project Structure

```text
task-12-13/
│
├── app/
│   └── main.py
│
├── Dockerfile
└── requirements.txt
```

---

## 1. Create FastAPI Application

### `app/main.py`

```python
import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    app_name = os.getenv("APP_NAME", "Default FastAPI App")

    return {
        "message": "Hello from Docker!",
        "app_name": app_name
    }


@app.get("/health")
def health():
    return {"status": "healthy"}
```

The application uses:

```python
os.getenv("APP_NAME")
```

to read the `APP_NAME` environment variable.

---

## 2. Create requirements.txt

### `requirements.txt`

```text
fastapi
uvicorn[standard]
```

These dependencies are required to run the FastAPI application.

---

## 3. Create Dockerfile

### `Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Dockerfile Instructions

| Instruction | Purpose |
|---|---|
| `FROM` | Uses Python 3.12 as the base image |
| `WORKDIR` | Sets `/app` as the working directory |
| `COPY` | Copies files into the Docker image |
| `RUN` | Installs Python dependencies |
| `EXPOSE` | Documents that the application uses port 8000 |
| `CMD` | Starts the FastAPI application |

---

# Task 12 — Install Dependencies Automatically

Build the Docker image:

```powershell
docker build -t super30-api .
```

During the build, Docker executes:

```dockerfile
RUN pip install --no-cache-dir -r requirements.txt
```

This automatically installs:

- FastAPI
- Uvicorn

inside the Docker image.

---

# Task 13 — Pass Environment Variable

Run the container with an environment variable:

```powershell
docker run -p 8000:8000 -e APP_NAME="Super30 FastAPI" super30-api
```

Here:

```text
-e APP_NAME="Super30 FastAPI"
```

passes the environment variable to the container.

The FastAPI application retrieves it using:

```python
os.getenv("APP_NAME")
```

---

## Test the Application

Open:

```text
http://localhost:8000
```

Expected response:

```json
{
    "message": "Hello from Docker!",
    "app_name": "Super30 FastAPI"
}
```

Swagger UI:

```text
http://localhost:8000/docs
```

---

## Verify Environment Variable

You can also verify the variable inside the container:

```powershell
docker run --rm -e APP_NAME="Super30 FastAPI" super30-api env
```

Look for:

```text
APP_NAME=Super30 FastAPI
```

---

## Key Concept

The complete flow is:

```text
requirements.txt
       │
       ▼
Dockerfile
       │
       ▼
docker build
       │
       ▼
Docker Image
       │
       │ -e APP_NAME="Super30 FastAPI"
       ▼
Docker Container
       │
       ▼
FastAPI Application
       │
       ▼
os.getenv("APP_NAME")
```

---

## Useful Commands

### Build image

```powershell
docker build -t super30-api .
```

### List images

```powershell
docker images
```

### Run container

```powershell
docker run -p 8000:8000 -e APP_NAME="Super30 FastAPI" super30-api
```

### List running containers

```powershell
docker ps
```

### Stop container

```powershell
docker stop <container_id>
```

### Remove container

```powershell
docker rm <container_id>
```

---

## Conclusion

Tasks 12 and 13 demonstrate how Docker can manage both **application dependencies and runtime configuration**.

- `requirements.txt` defines the Python dependencies.
- Docker installs them automatically during image creation.
- Environment variables allow configuration to be supplied when the container starts.
- Python's `os.getenv()` allows the FastAPI application to access those values.