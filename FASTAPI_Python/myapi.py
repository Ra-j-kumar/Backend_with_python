from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

student = {
    1 : {
        "name": "John",
        "age": 22,        
        "year" : "year 12"    
    }
}

class Student(BaseModel):
    name : str
    age : int
    year : str
    
class updatestudent(BaseModel):
    name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None
    
@app.get("/")
def index():
    return {"message": "Hello, World!"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return student[student_id]

@app.get("/get-by-name")
def get_student(name: str):
    for student_id in student:
        if student[student_id]["name"] == name:
            return student[student_id]        
    return {"Data": "Not Found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, students: Student):
    if student_id in student:
        return {"Error":"Student exists"}
    student[student_id] = students
    return student[student_id]

@app.put("/upate-student/{student_id}")
def update_student(student_id: int, students: Student):
    if student_id not in student:
        return {"Error":"Student does not exist"}
    student[student_id] = students
    return student[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in student:
        return {"Error":"Student does not exist"}
    del student[student_id]
    return {"Message": "student deleted"}