import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Dockerized FastAPI Application",
        "app_name": os.getenv("APP_NAME", "Default App"),
        "environment": os.getenv("APP_ENV", "unknown"),
        "version": os.getenv("APP_VERSION", "unknown")
    }


@app.get("/health")
def health():
    return {"status": "healthy"}