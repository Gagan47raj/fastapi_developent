from typing import List
from fastapi import FastAPI, APIRouter
from app.models.student import Student, Student_Response

from app.services.student_service import add_student


student_router = FastAPI()

student_router = APIRouter(
    prefix="/student"
)


@student_router.post("/add")
async def student_model(student : Student):

    student_data = student.model_dump()

    student_id = await add_student(student_data)

    return {
        "message":"Student added",
        "id" : str(student_id)
    }