import os

import psycopg2
from fastapi import FastAPI

app = FastAPI()


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("POSTGRES_DB", "super30db"),
        user=os.getenv("POSTGRES_USER", "super30user"),
        password=os.getenv("POSTGRES_PASSWORD", "super30password"),
    )


@app.get("/")
def home():
    return {
        "message": "FastAPI + PostgreSQL is running!"
    }


@app.get("/db-check")
def database_check():
    connection = get_connection()

    cursor = connection.cursor()
    cursor.execute("SELECT version();")

    version = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return {
        "database": "PostgreSQL",
        "status": "connected",
        "version": version
    }