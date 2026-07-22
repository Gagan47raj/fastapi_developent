from typing import Annotated, Optional

from pydantic import BaseModel, EmailStr, Field


class Student(BaseModel):
    name : str  = Field(..., min_length=3, max_length=50)
    rollno : int
    department : str
    cgpa : float = Field(..., gt=4)
    email : EmailStr
    phone : Annotated[str,Field(...,pattern=r"[6-9]\d{9}$")]
    aadhar : str = Field(..., pattern=r"^\d{12}$")
    pancard : str = Field(..., pattern=r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$")
    password : str = Field(..., min_length=8)

class Student_Response(BaseModel):
    name : str
    rollno : int
    department : str
    email : str


class Student_Update(BaseModel):
    name : Optional[str] = None
    rollno : Optional[int] = None
    department : Optional[str] = None
    email : Optional[EmailStr] = None
    password : Optional[str] = None
    phone : Optional[str] = None

class Student_Filtered(BaseModel):
    department : Optional[str] = None
    rollno : Optional[int] = None
    min_cgpa : Optional[float] = None
    max_cgpa : Optional[float] = None
    name : Optional[str] = None