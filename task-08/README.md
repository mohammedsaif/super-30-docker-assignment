Create a simple FastAPI application and containerize it using Docker.

1. create the app.py
2. dockerfile
update the dockerfile 
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

3. requirements.txt
fastapi
uvicorn

run the build commands

docker build -t super30-api .

docker images
