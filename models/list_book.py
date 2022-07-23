from models.book import Book
import datetime


book1 = Book("The Constitution of Liberty", "F. Hayek", "Economy", False, datetime.date(2022, 6, 17))
book2 = Book("Zero to One", "Peter Thiel", "Business", True, datetime.date(2022, 4, 7))
book3 = Book("Rich Dad, Poor Dad", "Robert Kiyosaki", "Finance", True, datetime.date(2022, 5, 23))


books = [book1, book2, book3]


def add_book(new_book):
    books.append(new_book)


def delete_book(book_title):
    for book in books:
        if book.title == book_title:
            books.remove(book)

