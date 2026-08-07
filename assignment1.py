class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Patron:
    def __init__(self, name):
        self.name = name
        self.books = []


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title):
        self.books.append(Book(title))

    def register_patron(self, name):
        self.patrons.append(Patron(name))

    def borrow_book(self, patron_name, book_title):
        patron = None
        book = None

        for p in self.patrons:
            if p.name == patron_name:
                patron = p

        for b in self.books:
            if b.title == book_title:
                book = b

        if patron and book and book.available:
            book.available = False
            patron.books.append(book.title)
            print("Book borrowed successfully")
        else:
            print("Book not available")

    def return_book(self, patron_name, book_title):
        for p in self.patrons:
            if p.name == patron_name and book_title in p.books:
                p.books.remove(book_title)
                for b in self.books:
                    if b.title == book_title:
                        b.available = True
                print("Book returned successfully")
                return
        print("Return failed")

    def show_books(self):
        for b in self.books:
            status = "Available" if b.available else "Borrowed"
            print(b.title, "-", status)


library = Library()

library.add_book("Python")
library.add_book("Java")

library.register_patron("Akshay")

library.borrow_book("Akshay", "Python")
library.show_books()

library.return_book("Akshay", "Python")
library.show_books()