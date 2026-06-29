def get_return_book(books: list, is_available_endpoint: bool) -> list:
    return list(filter(lambda book: book["is_available"] == is_available_endpoint, books))