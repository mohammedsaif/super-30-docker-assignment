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