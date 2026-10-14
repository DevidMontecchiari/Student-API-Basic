"""Read fictional Student records. Start the application with: python run.py"""

import json
from pathlib import Path

from fastapi import FastAPI, HTTPException

app = FastAPI(title="Student API")

# Locate the JSON beside this Python file, even from another working directory.
STUDENTS_FILE = Path(__file__).resolve().parent / "data" / "students.json"


def load_students():
    # json.load converts the JSON array into a Python list of dictionaries.
    # 'with' closes the file when this indented block finishes.
    with STUDENTS_FILE.open(encoding="utf-8") as file:
        return json.load(file)


# A decorator connects an HTTP method and URL path to the function below it.
@app.get("/")
def root():
    return {"message": "Welcome to the Student API!", "documentation": "/docs"}


@app.get("/students")
def list_students():
    # Load on every request, so a saved edit to the JSON is visible immediately.
    return load_students()


@app.get("/students/{student_id}")
def get_student(student_id: int):
    # FastAPI reads the URL value and validates/converts it to an integer.
    students = load_students()
    for student in students:
        # [] reads a dictionary entry; == compares two values.
        if student["student_id"] == student_id:
            return student  # return ends the function; FastAPI sends JSON.

    # Outside the loop: report 'not found' only after checking every student.
    raise HTTPException(status_code=404, detail="Student not found")
