from lib import *
from fastapi import FastAPI
import utils

app = FastAPI(title="Library API")


@app.get("/health")
def health_check():
    return {"message": "Library API is running"}


@app.get("/books")      
def get_books():
    return books

# Sử dụng lambda
# @app.get("/books/available")
# def get_available_books(books, True):
#     return_books = utils.get_return_book(books, True)

# Sử dụng list comprehension
@app.get("/books/available")
def get_available_books():
    result = [book for book in books if book["is_available"] == True]
    return result

@app.get("/books/borrowed")
def get_borrowed_books():
    result = [book for book in books if book["is_available"] == False]
    return result


# Sử dụng vòng lặp for
# 

# @app.get("/books/available")
# def get_available_books():
#     result = []
#     for book in books:
#         if book["is_available"] == True:
#             result.append(book)
#     return result


# @app.get("/books/borrowed")
# def get_borrowed_books():
#     result = []
#     for book in books:
#         if book["is_available"] == False:
#             result.append(book)
#     return result