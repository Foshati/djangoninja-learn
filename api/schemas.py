from typing import Optional
from ninja import Field, FilterSchema, ModelSchema
from .models import Book


class BookSchema(ModelSchema):
    class Config:
        model = Book
        model_fields = "__all__"


class BookFindSchema(FilterSchema):
    name: Optional[str] = Field(None, q="name__startswith")
    author: Optional[str] = None
