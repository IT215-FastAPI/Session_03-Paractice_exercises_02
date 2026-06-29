def get_return_book(book: list, is_available_endpoint: True):
   list(filter(lambda book: book["is_available"] if is_available_endpoint else not book["is_available"], book))