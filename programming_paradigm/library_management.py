# class Book:
#     def __init__(self, title,author):
#         self.title = title
#         self.author = author
#         self._is_checked_out = 0
        
# class Library:
#     def __init__(self, books):
#         self.books = list(books)
        
#     def add_book(self, book):
#         self.books.append(book)
        
#     def check_out_book(self, title):


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Marks the book as returned (available)."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is not checked out."""
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a Book instance to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Finds a book by title and checks it out if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        """Finds a book by title and marks it as returned."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' is not currently checked out.")

    def list_available_books(self):
        """Prints all available books."""
        for book in self._books:
            if book.is_available():
                print(book)
