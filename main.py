from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Welcome to fastAPI development"

# home, contact, about

@app.get("/home")
def home():
    return "Home Page"

# synchronous api
@app.get("/about")
def about():
    return "About Page"

#asynchronous api
@app.get("/async")
async def async_api():
    return "Async API"

@app.post("/post")
def post_api():
    return "Post API"

@app.put("/put")
def put_api():
    return "Put API"

@app.delete("/delete")
def delete_api():
    return "Delete API"

@app.get("/getdata")
def get_student_data():
    students = [
        {"name" : "aman", "roll no":21, "dept" : "cse"},
        {"name" : "amit", "roll no":22, "dept" : "cse"}
    ]

    return students

#path parameter : to get specific result
@app.get("/getdata/{id:int}")
def path_param(id):
    return f"student id : {id}"

# create student list with name
# if entered name is in list/data simply return it 
# otherwise return message data not found


#query parameter : to get filtered or sorted result
# ?department=It&cgpa=5

#/student?department=CSE&cgpa=5.5
@app.get("/student")
def get_query(department : str, cgpa : float):
    
    students = [
        {"name" : "aman", "roll no":21, "dept" : "cse", "cgpa" : 5.5},
        {"name" : "amit", "roll no":22, "dept" : "cse", "cgpa" : 6.5},
        {"name" : "amit", "roll no":22, "dept" : "ece", "cgpa" : 6.5},
        {"name" : "amit", "roll no":22, "dept" : "civil", "cgpa" : 6.5},
    ]

    result = []

    #acc to query parameter print result
    # cgpa => 5.5 department = cse

    return result


#Pydantic : validation tool by which
# python automatically validate request and response 

from pydantic import BaseModel, EmailStr, Field
from typing import Annotated

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
    # abcde1234a

class Student_Response(BaseModel):
    name : str
    rollno : int
    department : str
    email : str



students=[]

@app.post("/student/add", response_model=Student_Response)
def student_model(student : Student):

    students.append(student)

    return f"Student Added : {students}"

@app.get("/student/get", response_model=Student_Response)
def getStudentDetails():
    student_detail = {"name":"amit", "rollno":21, "department":"CSE", "email" : "amit@gmail.com", "password" : "1234abcd"}

    return student_detail

# Field : apply explicit valid 
# name : must be greater than 3 char max 50
# cgpa : must be greater than 4
 

