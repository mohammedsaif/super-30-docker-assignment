from fastapi import FastAPI

app = FastAPI(title="Super30 FastAPI App")


@app.get("/")
def home():
    return {
        "message": "Hello from Super30 FastAPI!",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }