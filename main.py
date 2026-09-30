from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


app = FastAPI()

class Student (BaseModel):
    name: str
    age: int
    roll: int

@app.get("/")
def read_root():
    return {"message": "hello world"}

@app.get("/greet")
def greet():
    return {"message":"hello greet"}

@app.get("/greet/{name}")
def greet_name(name: str , age: Optional[int] = None,):
    return {"message":f"hello {name} and you have {age} years old"}


@app.post("/create_student")
def create_student(student: Student):
    return {
        "name" : student.name,
        "age" : student.age,
        "roll" : student.roll
    }


    