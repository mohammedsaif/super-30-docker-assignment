import os
import time
from contextlib import contextmanager
from typing import List, Optional

import psycopg2
from fastapi import FastAPI, HTTPException, Query, Response
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel


class StudentIn(BaseModel):
    name: str
    email: str
    course: str
    age: int


class Student(StudentIn):
    id: int


def connect():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("POSTGRES_DB", "studentdb"),
        user=os.getenv("POSTGRES_USER", "studentuser"),
        password=os.getenv("POSTGRES_PASSWORD", "studentpassword"),
    )


@contextmanager
def cursor():
    conn = connect()
    try:
        with conn, conn.cursor(cursor_factory=RealDictCursor) as cur:
            yield cur
    finally:
        conn.close()


def init_db(retries: int = 10) -> None:
    for attempt in range(retries):
        try:
            with cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS students (
                        id SERIAL PRIMARY KEY,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE,
                        course TEXT NOT NULL,
                        age INTEGER NOT NULL
                    )
                    """
                )
            return
        except psycopg2.OperationalError:
            if attempt == retries - 1:
                raise
            time.sleep(2)


app = FastAPI(title="Student Management System")


@app.on_event("startup")
def startup() -> None:
    init_db()


@app.get("/health")
def health():
    try:
        with cursor() as cur:
            cur.execute("SELECT 1")
    except psycopg2.Error:
        raise HTTPException(status_code=503, detail="database unavailable")
    return {"status": "healthy", "database": "connected"}


@app.post("/students", response_model=Student, status_code=201)
def create_student(student: StudentIn):
    try:
        with cursor() as cur:
            cur.execute(
                "INSERT INTO students (name, email, course, age) "
                "VALUES (%s, %s, %s, %s) RETURNING *",
                (student.name, student.email, student.course, student.age),
            )
            return cur.fetchone()
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Email already exists")


@app.get("/students", response_model=List[Student])
def list_students(search: Optional[str] = Query(None)):
    with cursor() as cur:
        if search:
            like = f"%{search}%"
            cur.execute(
                "SELECT * FROM students WHERE name ILIKE %s OR email ILIKE %s "
                "OR course ILIKE %s ORDER BY id",
                (like, like, like),
            )
        else:
            cur.execute("SELECT * FROM students ORDER BY id")
        return cur.fetchall()


@app.get("/students/{student_id}", response_model=Student)
def get_student(student_id: int):
    with cursor() as cur:
        cur.execute("SELECT * FROM students WHERE id = %s", (student_id,))
        row = cur.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return row


@app.put("/students/{student_id}", response_model=Student)
def update_student(student_id: int, student: StudentIn):
    try:
        with cursor() as cur:
            cur.execute(
                "UPDATE students SET name=%s, email=%s, course=%s, age=%s "
                "WHERE id=%s RETURNING *",
                (student.name, student.email, student.course, student.age, student_id),
            )
            row = cur.fetchone()
    except psycopg2.errors.UniqueViolation:
        raise HTTPException(status_code=409, detail="Email already exists")
    if row is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return row


@app.delete("/students/{student_id}", status_code=204)
def delete_student(student_id: int):
    with cursor() as cur:
        cur.execute("DELETE FROM students WHERE id = %s", (student_id,))
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Student not found")
    return Response(status_code=204)
