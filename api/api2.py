# from typing import List
# from django.shortcuts import get_object_or_404
# from ninja import NinjaAPI, Schema
# from ninja.router import Router
# from .models import Book
# from .schemas import BookSchema

# app = NinjaAPI(title="Book API", version="1.0.2")


# class NotFoundSchema(Schema):
#     message: str


# class SuccessMessageSchema(Schema):
#     message: str


# class ErrorMessageSchema(Schema):
#     message: str


# class BookAPI:
#     router = Router()

#     @router.post(
#         "/books",
#         response={201: BookSchema, 400: ErrorMessageSchema, 500: ErrorMessageSchema},
#     )
#     def create_book(self, request, payload: BookSchema):
#         try:
#             book = Book.objects.create(**payload.dict())
#             return 201, book
#         except Exception as e:
#             return 500, {"message": str(e)}

#     @router.get(
#         "/books",
#         response={200: List[BookSchema], 404: NotFoundSchema, 500: ErrorMessageSchema},
#     )
#     def list_books(self, request):
#         try:
#             books = Book.objects.all()
#             if not books:
#                 return 404, {"message": "No books found."}
#             return 200, books
#         except Exception as e:
#             return 500, {"message": str(e)}

#     @router.get(
#         "/books/{book_id}",
#         response={200: BookSchema, 404: NotFoundSchema, 500: ErrorMessageSchema},
#     )
#     def single_book(self, request, book_id: int):
#         try:
#             book = get_object_or_404(Book, id=book_id)
#             return 200, book
#         except Book.DoesNotExist:
#             return 404, {"message": "Book not found."}
#         except Exception as e:
#             return 500, {"message": str(e)}

#     @router.patch(
#         "/books/{book_id}",
#         response={200: BookSchema, 404: NotFoundSchema, 500: ErrorMessageSchema},
#     )
#     def update_book(self, request, book_id: int, payload: BookSchema):
#         try:
#             book = get_object_or_404(Book, id=book_id)
#             for attr, value in payload.dict().items():
#                 setattr(book, attr, value)
#             book.save()
#             return 200, book
#         except Book.DoesNotExist:
#             return 404, {"message": "Book not found."}
#         except Exception as e:
#             return 500, {"message": str(e)}

#     @router.delete(
#         "/books/{book_id}",
#         response={
#             200: SuccessMessageSchema,
#             404: NotFoundSchema,
#             500: ErrorMessageSchema,
#         },
#     )
#     def delete_book(self, request, book_id: int):
#         try:
#             book = get_object_or_404(Book, id=book_id)
#             book.delete()
#             return 200, {"message": "The book was deleted."}
#         except Book.DoesNotExist:
#             return 404, {"message": "Book not found."}
#         except Exception as e:
#             return 500, {"message": str(e)}


# app.add_router("/", BookAPI.router)
