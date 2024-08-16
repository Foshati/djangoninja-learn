from typing import Any, List, Optional
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import File, NinjaAPI, Query, UploadedFile
from ninja.security import APIKeyQuery
from test.test_zoneinfo import valid_keys
from .models import Book
from .schemas import BookFindSchema, BookSchema
from ninja.throttling import AnonRateThrottle


# API Key for security
# /books/?api_key=***
# http://127.0.0.1:8000/api/books?foshati=key1234
class ApiKey(APIKeyQuery):
    param_name = "foshati"

    def authenticate(self, request, key: Optional[str]) -> Optional[Any]:
        valid_keys = ["key1", "key1234"]
        if key in valid_keys:
            return {"key": key}
        else:
            return None


api_key = ApiKey()
app = NinjaAPI(title="Book API", version="1.0.2", auth=api_key)


@app.post("/books", response=BookSchema)
def create_book(request, payload: BookSchema):
    book = Book.objects.create(**payload.dict())
    return book


@app.get(
    "/books",
    response=List[BookSchema],
    auth=None,
    throttle=[AnonRateThrottle("60/hour")],
)
def list_books(request: HttpRequest):
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
# __icontains This is a case-insensitive search filter.
# __contains This is a case-sensitive search filter =>  a | A
@app.get("/books/search/", response=List[BookSchema])
def search_book(request, query: str):
    book = Book.objects.filter(Q(name__icontains=query) | Q(author__icontains=query))
    return book


# filter search
@app.get("/books/find/", response=List[BookSchema])
def find_book(request, find: BookFindSchema = Query(...)):
    books = Book.objects.all()
    book = find.filter(books)
    # print(find.get_filter_expression())
    return book


@app.post("upload")
def upload_img_book(request, file: UploadedFile = File(...)):
    data = file.read()
    return {"file_name": file.name, "len": len(data)}
