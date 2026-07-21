from typing import List
from fastapi import FastAPI, APIRouter
from app.models.student import Student, Student_Response


student_router = FastAPI()

student_router = APIRouter(
    prefix="/student"
)

students = []

@student_router.post("/add", response_model=List[Student_Response])
def student_model(student : Student):

    students.append(student)

    return students