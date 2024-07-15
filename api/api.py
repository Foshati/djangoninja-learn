from typing import List
from ninja import NinjaAPI
from .models import Book
from .schemas import BookSchema

app = NinjaAPI()


@app.post("/books", response=BookSchema)
def create_book(request, payload: BookSchema):
    book = Book.objects.create(**payload.dict())
    return book


@app.get("/books", response=List[BookSchema])
def list_books(request):
    books = Book.objects.all()
    return books
