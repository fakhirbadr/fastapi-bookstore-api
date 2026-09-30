
from fastapi import FastAPI , status
from pydantic import BaseModel
from fastapi.exceptions import HTTPException

books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publish_date": "2008-08-01",
        "added_by": "Badr"
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "David Thomas",
        "publish_date": "1999-10-20",
        "added_by": "Badr"
    },
    {
        "id": 3,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publish_date": "2015-11-01",
        "added_by": "Admin"
    },
    {
        "id": 4,
        "title": "Deep Learning",
        "author": "Ian Goodfellow",
        "publish_date": "2016-11-18",
        "added_by": "Admin"
    },
    {
        "id": 5,
        "title": "Artificial Intelligence: A Modern Approach",
        "author": "Stuart Russell",
        "publish_date": "2020-04-28",
        "added_by": "Badr"
    },
    {
        "id": 6,
        "title": "Design Patterns",
        "author": "Erich Gamma",
        "publish_date": "1994-10-31",
        "added_by": "Admin"
    },
    {
        "id": 7,
        "title": "Introduction to Algorithms",
        "author": "Thomas H. Cormen",
        "publish_date": "2009-07-31",
        "added_by": "Badr"
    },
    {
        "id": 8,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publish_date": "2015-08-20",
        "added_by": "Admin"
    },
    {
        "id": 9,
        "title": "Hands-On Machine Learning",
        "author": "Aurélien Géron",
        "publish_date": "2017-03-13",
        "added_by": "Badr"
    },
    {
        "id": 10,
        "title": "The Lean Startup",
        "author": "Eric Ries",
        "publish_date": "2011-09-13",
        "added_by": "Admin"
    }
]

app = FastAPI()

@app.get("/books")
def get_books():
    return books

@app.get("/book/{book_id}")
def get_books(book_id : int):
    for book in books:
        if book ['id'] == book_id:
         return book

    raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.post("/book")
def create_book( book : Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book