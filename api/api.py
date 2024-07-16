from email import message
from typing import List
from django.shortcuts import get_object_or_404
from ninja import NinjaAPI
from .models import Book
from .schemas import BookSchema

app = NinjaAPI(title="Book API", version="1.0.2")


@app.post("/books", response=BookSchema)
def create_book(request, payload: BookSchema):
    book = Book.objects.create(**payload.dict())
    return book


@app.get("/books", response=List[BookSchema])
def list_books(request):
    books = Book.objects.all()
    return books


@app.get("/books/{book_id}", response=BookSchema)
def single_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    return book


@app.patch("/books/{book_id}", response=BookSchema)
def update_book(request, book_id: int, payload: BookSchema):
    book = get_object_or_404(Book, id=book_id)
    for attr, value in payload.dict().items():
        setattr(book, attr, value)
    book.save()
    return book


@app.delete("/books/{book_id}")
def deleted_book(request, book_id: int):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return {"message": "the book was deleted"}


# GET /book/search?query=school
